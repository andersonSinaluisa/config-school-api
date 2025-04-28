from rest_framework.viewsets import ViewSet

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.subject_serializer import SubjectSerializer
from core.container import Container
from rest_framework.response import Response
from rest_framework import status


class SubjectViewSet(ViewSet):
    """
    A viewset for managing subjects.
    """
    serializer_class = SubjectSerializer
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_subject_service = Container.create_subject_service()
        self.delete_subject_service = Container.delete_subject_service()
        self.update_subject_service = Container.update_subject_service()
        self.get_subject_service = Container.get_subject_service()
        self.list_subject_service = Container.list_subject_service()

    
    
    def create(self, request):
        """
        Create a new subject.
        Expects a JSON payload with subject details.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = self.create_subject_service.execute(
            **serializer.validated_data)
        return Response(self.serializer_class(subject).data, status=status.HTTP_201_CREATED)
    
    
    def list(self, request):
        """
        List all subjects.
        """
        subjects = self.list_subject_service.execute()
        paginator = StandardResultsSetPagination(request, subjects)
        paginated_data = paginator.paginate_queryset()

        serializer = self.serializer_class(paginated_data, many=True)

        return paginator.get_paginated_response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        """
        Retrieve a subject by its ID.
        """
        subject = self.get_subject_service.execute(pk)
        serializer = self.serializer_class(subject)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        """
        Update a subject by its ID.
        Expects a JSON payload with updated subject details.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = self.update_subject_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(subject).data, status=status.HTTP_200_OK)
    
    
    def destroy(self, request, pk=None):
        """
        Delete a subject by its ID.
        """
        self.delete_subject_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)