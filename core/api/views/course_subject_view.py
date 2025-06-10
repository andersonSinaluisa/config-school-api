from rest_framework.viewsets import ViewSet

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.course_subject_serializer import CourseSubjectSerializer
from core.container import Container
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class CourseSubjectAPIView(APIView):
    serializer_class = CourseSubjectSerializer

    
    def __init__(self, **kwargs):
        self.list_subjects_from_course = Container.list_subjects_from_course()
        self.create_range_course_subject_service = Container.create_range_course_subject_service()
        self.remove_from_course_service = Container.remove_from_course_service()
        self.remove_range_course_subject_service = Container.remove_range_from_course_service()
        super().__init__(**kwargs)
    def get(self, request, course_id):
        """
        List all subjects for a specific course.
        """
        subjects = self.list_subjects_from_course.execute(course_id)

        serializer = self.serializer_class(subjects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, course_id):
        """
        Assign a subject to a course.
        """
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        
        result = self.create_range_course_subject_service.execute(
            course_id,serializer.validated_data)
        
        serializer = self.serializer_class(result, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    





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