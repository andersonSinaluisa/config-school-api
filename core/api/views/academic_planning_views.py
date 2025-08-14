from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.academic_planning_serializer import AcademicPlanningSerializer
from core.container import Container


class AcademicPlanningViewSet(ViewSet):
    serializer_class = AcademicPlanningSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_planning_service = Container.create_academic_planning_service()
        self.list_planning_service = Container.list_academic_planning_service()
        self.get_planning_service = Container.get_academic_planning_service()
        self.update_planning_service = Container.update_academic_planning_service()
        self.delete_planning_service = Container.delete_academic_planning_service()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        planning = self.create_planning_service.execute(**serializer.validated_data)
        return Response(self.serializer_class(planning).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        course_id = request.query_params.get('course_id', None)
        parallel_id = request.query_params.get('parallel_id', None)
        school_year_id = request.query_params.get('school_year_id', None)
        subject_id = request.query_params.get('subject_id', None)
        topic = request.query_params.get('topic', None)
        plannings = self.list_planning_service.execute(
            course_id=course_id,
            parallel_id=parallel_id,
            school_year_id=school_year_id,
            subject_id=subject_id,
            topic=topic,
        )
        paginator = StandardResultsSetPagination(request, plannings)
        paginated_data = paginator.paginate_queryset()
        serializer = self.serializer_class(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        planning = self.get_planning_service.execute(pk)
        serializer = self.serializer_class(planning)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        planning = self.update_planning_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(planning).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.delete_planning_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
