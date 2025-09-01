from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.section_break_serializer import SectionBreakSerializer
from core.container import Container


class SectionBreakViewSet(ViewSet):
    serializer_class = SectionBreakSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_service = Container.create_section_break_service()
        self.list_service = Container.list_section_break_service()
        self.get_service = Container.get_section_break_service()
        self.update_service = Container.update_section_break_service()
        self.delete_service = Container.delete_section_break_service()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.create_service.execute(**serializer.validated_data)
        return Response(self.serializer_class(obj).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        section_id = request.query_params.get('section_id', None)
        objs = self.list_service.execute(section_id=section_id)
        paginator = StandardResultsSetPagination(request, objs)
        page = paginator.paginate_queryset()
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = self.get_service.execute(pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.update_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(obj).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.delete_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

