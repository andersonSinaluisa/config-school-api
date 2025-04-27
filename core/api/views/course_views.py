"""
Course API Views
"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from core.application.serializers.course_serializer import CourseSerializer
from core.container import Container
from rest_framework.exceptions import NotFound

class CourseViewSet(ViewSet):
    """
    APIView for creating a new course.

    Args:
        APIView ([APIView]): Inherits from Django Rest Framework's APIView.
        serializer_class ([CourseSerializer]): Serializer class for course data validation and serialization.

    Returns:
        [Response]: Returns a response with the created course data or an error message.
    This APIView provides actions to create a new course.
    """
    serializer_class = CourseSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_course_service = Container.create_course_service()
        self.list_course_service = Container.list_course_service()
        self.get_course_service = Container.get_course_service()
        self.update_course_service = Container.update_course_service()
        self.delete_course_service = Container.delete_course_service()

    def create(self, request):
        '''
        Create a new course.
        Expects a JSON payload with course details.
        '''

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        course = self.create_course_service.execute(
            **serializer.validated_data)
        return Response(self.serializer_class(course).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        '''
        List all courses.
        '''
        courses = self.list_course_service.execute()
        serializer = self.serializer_class(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk=None):
        '''
        Retrieve a course by its ID.
        '''
        course = self.get_course_service.execute(pk)


        serializer = self.serializer_class(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
        


    def update(self, request, pk=None):
        '''
        Update a course by its ID.
        Expects a JSON payload with updated course details.
        '''
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            course = self.update_course_service.execute(
                pk, **serializer.validated_data)
            return Response(self.serializer_class(course).data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def destroy(self, request, pk=None):
        '''
        Delete a course by its ID.
        '''
        try:
            print('pk', pk)
            self.delete_course_service.execute(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)
