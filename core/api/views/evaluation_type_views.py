from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.evaluation_type_serializer import EvaluationTypeSerializer
from core.container import Container


class EvaluationTypeViewSet(ViewSet):
    """ViewSet for managing evaluation types."""
    serializer_class = EvaluationTypeSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_evaluation_type_service = Container.create_evaluation_type_service()
        self.delete_evaluation_type_service = Container.delete_evaluation_type_service()
        self.get_evaluation_type_service = Container.get_evaluation_type_service()
        self.list_evaluation_type_service = Container.list_evaluation_type_service()
        self.update_evaluation_type_service = Container.update_evaluation_type_service()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        evaluation_type = self.create_evaluation_type_service.execute(**serializer.validated_data)
        return Response(self.serializer_class(evaluation_type).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        evaluation_types = self.list_evaluation_type_service.execute()
        paginator = StandardResultsSetPagination(request, evaluation_types)
        paginated_data = paginator.paginate_queryset()
        serializer = self.serializer_class(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        evaluation_type = self.get_evaluation_type_service.execute(pk)
        serializer = self.serializer_class(evaluation_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        evaluation_type = self.update_evaluation_type_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(evaluation_type).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.delete_evaluation_type_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
