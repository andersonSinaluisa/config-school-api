from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.behavior_scale_serializer import BehaviorScaleSerializer
from core.container import Container


class BehaviorScaleViewSet(ViewSet):
    """ViewSet for managing behavior scales."""
    serializer_class = BehaviorScaleSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_behavior_scale_service = Container.create_behavior_scale_service()
        self.delete_behavior_scale_service = Container.delete_behavior_scale_service()
        self.get_behavior_scale_service = Container.get_behavior_scale_service()
        self.list_behavior_scale_service = Container.list_behavior_scale_service()
        self.update_behavior_scale_service = Container.update_behavior_scale_service()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        behavior_scale = self.create_behavior_scale_service.execute(**serializer.validated_data)
        return Response(self.serializer_class(behavior_scale).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        behavior_scales = self.list_behavior_scale_service.execute()
        paginator = StandardResultsSetPagination(request, behavior_scales)
        paginated_data = paginator.paginate_queryset()
        serializer = self.serializer_class(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        behavior_scale = self.get_behavior_scale_service.execute(pk)
        serializer = self.serializer_class(behavior_scale)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        behavior_scale = self.update_behavior_scale_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(behavior_scale).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.delete_behavior_scale_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
