from rest_framework.viewsets import ViewSet

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.parallel_serializer import ParallelSerializer
from core.container import Container
from rest_framework.response import Response
from rest_framework import status


class ParallelViewSet(ViewSet):
    """
    A viewset that handles parallel requests.
    """
    serializer_class = ParallelSerializer
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_parallel = Container.create_parallel_service()
        self.update_parallel = Container.update_parallel_service()
        self.delete_parallel = Container.delete_parallel_service()
        self.get_parallel = Container.get_parallel_service()
        self.get_all_parallels = Container.list_parallel_service()
        self.get_all_parallels_by_course = Container.list_parallel_by_course_service()
    def list(self, request, *args, **kwargs):
        
        """
        Handle GET requests to list all resources.
        """
      
        course_id = request.query_params.get('course_id', None)
        school_year_id = request.query_params.get('school_year_id', None)
        name = request.query_params.get('name', None)
        capacity = request.query_params.get('capacity', None)
        section_id = request.query_params.get('section_id', None)
        # Implement your logic here
        parallels = self.get_all_parallels.execute(
            course_id=course_id,
            school_year_id=school_year_id,
            name=name,
            capacity=capacity,
            section_id=section_id
        )
        paginator = StandardResultsSetPagination(request, parallels)
        paginated_data = paginator.paginate_queryset()

        serializer = self.serializer_class(paginated_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Handle POST requests to create a resource.
        """
        # Implement your logic here
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        parallel = self.create_parallel.execute(
            **serializer.validated_data)
        return Response(self.serializer_class(parallel).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a specific resource.
        """
        # Implement your logic here
        parallel_id = kwargs.get('pk')
        parallel = self.get_parallel.execute(parallel_id)
        response = self.serializer_class(parallel)
        return Response(response.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """
        Handle PUT/PATCH requests to update a specific resource.
        """
        # Implement your logic here
        parallel_id = kwargs.get('pk')
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        parallel = self.update_parallel.execute(parallel_id, **serializer.validated_data)
        return Response(self.serializer_class(parallel).data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete a specific resource.
        """
        # Implement your logic here
        parallel_id = kwargs.get('pk')
        self.get_parallel.execute(parallel_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
