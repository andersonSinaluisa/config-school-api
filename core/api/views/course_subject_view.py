from rest_framework.viewsets import ViewSet

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.course_subject_serializer import CourseSubjectSerializer
from core.container import Container
from rest_framework.response import Response
from rest_framework import status


class CourseSubjectViewSet(ViewSet):
    """
    A viewset for managing course subjects.
    """
    serializer_class = CourseSubjectSerializer

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_course_subject_service = Container.create_course_subject_service()
        self.delete_course_subject_service = Container.delete_course_subject_service()
        self.list_course_subject_service = Container.list_course_subject_service()
        self.get_course_subject_service = Container.get_course_subject_service()
        self.update_course_subject_service = Container.update_course_subject_service()
        
        
    def list(self, request):
        """
        List all course subjects.
        """
        course_subjects = self.list_course_subject_service.execute()
        paginator = StandardResultsSetPagination(request, course_subjects)
        paginated_data = paginator.paginate_queryset()

        serializer = self.serializer_class(paginated_data, many=True)

        return paginator.get_paginated_response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        """
        Retrieve a specific course subject by ID.
        """
        course_subject = self.get_course_subject_service.execute(pk)
        serializer = self.serializer_class(course_subject)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def create(self, request):
        """
        Create a new course subject.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        course_subject = self.create_course_subject_service.execute(**serializer.validated_data)
        return Response(self.serializer_class(course_subject).data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, pk=None):
        """
        Update an existing course subject.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        course_subject = self.update_course_subject_service.execute(pk, serializer.validated_data)
        return Response(self.serializer_class(course_subject).data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        """
        Delete a course subject.
        """
        self.delete_course_subject_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)