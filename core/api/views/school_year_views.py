
from rest_framework.viewsets  import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.school_year_serializer import SchoolYearSerializer
from core.container import Container

class SchoolYearViewSet(ViewSet):
    
    serializer_class = SchoolYearSerializer
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_school_year_service = Container.create_school_year_service()
        self.list_school_year_service = Container.list_school_year_service()
        self.get_school_year_service = Container.get_school_year_service()
        self.update_school_year_service = Container.update_school_year_service()
        self.delete_school_year_service = Container.delete_school_year_service()
        
        
    def create(self, request, *args, **kwargs):
        """
        Create a new school year.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        school_year = self.create_school_year_service.execute(**serializer.validated_data)
        
        return Response(self.serializer_class(school_year).data, status=status.HTTP_201_CREATED)
    
    
    def list(self, request, *args, **kwargs):
        """
        List all school years.
        """
        school_years = self.list_school_year_service.execute()
        paginator = StandardResultsSetPagination(request, school_years)
        paginated_data = paginator.paginate_queryset()

        serializer = self.serializer_class(paginated_data, many=True)

        return paginator.get_paginated_response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        """
        Retrieve a specific school year by ID.
        """
        school_year = self.get_school_year_service.execute(pk)
        serializer = self.serializer_class(school_year)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    def update(self, request, pk=None):
        """
        Update a specific school year by ID.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        school_year = self.update_school_year_service.execute(pk, **serializer.validated_data)
        return Response(school_year.to_dict(), status=status.HTTP_200_OK)
    
    
    def destroy(self, request, pk=None):
        """
        Delete a specific school year by ID.
        """
        self.delete_school_year_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    