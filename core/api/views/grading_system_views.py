from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.grading_system_serializer import GradingSystemSerializer
from core.container import Container


class GradingSystemViewSet(ViewSet):
    """ViewSet for managing grading systems."""
    serializer_class = GradingSystemSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_grading_system_service = Container.create_grading_system_service()
        self.delete_grading_system_service = Container.delete_grading_system_service()
        self.get_grading_system_service = Container.get_grading_system_service()
        self.list_grading_system_service = Container.list_grading_system_service()
        self.update_grading_system_service = Container.update_grading_system_service()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        grading_system = self.create_grading_system_service.execute(**serializer.validated_data)
        return Response(self.serializer_class(grading_system).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        grading_systems = self.list_grading_system_service.execute()
        paginator = StandardResultsSetPagination(request, grading_systems)
        paginated_data = paginator.paginate_queryset()
        serializer = self.serializer_class(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        grading_system = self.get_grading_system_service.execute(pk)
        serializer = self.serializer_class(grading_system)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        grading_system = self.update_grading_system_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(grading_system).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.delete_grading_system_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
