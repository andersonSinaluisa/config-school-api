from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

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

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        schedule = self.create_schedule_service.execute(**serializer.validated_data)
        return Response(self.serializer_class(schedule).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        schedules = self.list_schedule_service.execute()
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

