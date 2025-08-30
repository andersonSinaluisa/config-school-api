from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.class_schedule_serializer import ClassScheduleSerializer
from core.container import Container


class ClassScheduleViewSet(ViewSet):
    serializer_class = ClassScheduleSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_schedule_service = Container.create_class_schedule_service()
        self.list_schedule_service = Container.list_class_schedule_service()
        self.get_schedule_service = Container.get_class_schedule_service()
        self.update_schedule_service = Container.update_class_schedule_service()
        self.delete_schedule_service = Container.delete_class_schedule_service()
        self.generate_schedule_service = Container.generate_class_schedule_service()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        schedule = self.create_schedule_service.execute(**serializer.validated_data)
        return Response(self.serializer_class(schedule).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        course_id = request.query_params.get('course_id', None)
        parallel_id = request.query_params.get('parallel_id', None)
        school_year_id = request.query_params.get('school_year_id', None)
        subject_id = request.query_params.get('subject_id', None)
        day_of_week = request.query_params.get('day_of_week', None)
        schedules = self.list_schedule_service.execute(
            course_id=course_id,
            parallel_id=parallel_id,
            school_year_id=school_year_id,
            subject_id=subject_id,
            day_of_week=day_of_week,
        )
        paginator = StandardResultsSetPagination(request, schedules)
        paginated_data = paginator.paginate_queryset()
        serializer = self.serializer_class(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        schedule = self.get_schedule_service.execute(pk)
        serializer = self.serializer_class(schedule)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        schedule = self.update_schedule_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(schedule).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.delete_schedule_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=False, methods=['post'])
    def generate(self, request):
        parallel_id = request.data.get('parallel_id')
        if not parallel_id:
            return Response({"error": "parallel_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        schedules = self.generate_schedule_service.execute(parallel_id)
        serializer = self.serializer_class(schedules, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)