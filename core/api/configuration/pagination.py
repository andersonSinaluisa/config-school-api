from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    def __init__(self, request, data, page_size=5):
        self.request = request
        self.data = data
        self.page_size = int(request.query_params.get('limit', page_size))
        self.page = int(request.query_params.get('page', 1))
        self.search = request.query_params.get('search', None)
        self.sort = request.query_params.get('sort', None)
        self.total = len(data)
        self.last_page = (self.total + self.page_size - 1) // self.page_size

    def paginate_queryset(self):
        start = (self.page - 1) * self.page_size
        end = start + self.page_size
        if self.search:
            self.data = [item for item in self.data if self.search.lower() in str(item).lower()]
            self.total = len(self.data)
            self.last_page = (self.total + self.page_size - 1) // self.page_size
        if self.sort:
            self.data = sorted(self.data, key=lambda x: getattr(x, self.sort), reverse=True if self.sort.startswith('-') else False)
       
        return self.data[start:end]

    def get_paginated_response(self, serialized_data):
        return Response({
            'data': serialized_data,
            'meta': {
                'total': self.total,
                'lastPage': self.last_page,
                'currentPage': self.page,
                'perPage': self.page_size,
                'prev': self.page - 1 if self.page > 1 else None,
                'next': self.page + 1 if self.page < self.last_page else None,
            }
        }, headers={'Access-Control-Allow-Origin': '*'})