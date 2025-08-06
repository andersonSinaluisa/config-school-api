from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.meeting_type_serializer import MeetingTypeSerializer
from core.container import Container


class MeetingTypeViewSet(ViewSet):
    """ViewSet for managing meeting types."""
    serializer_class = MeetingTypeSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_meeting_type_service = Container.create_meeting_type_service()
        self.delete_meeting_type_service = Container.delete_meeting_type_service()
        self.get_meeting_type_service = Container.get_meeting_type_service()
        self.list_meeting_type_service = Container.list_meeting_type_service()
        self.update_meeting_type_service = Container.update_meeting_type_service()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        meeting_type = self.create_meeting_type_service.execute(**serializer.validated_data)
        return Response(self.serializer_class(meeting_type).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        meeting_types = self.list_meeting_type_service.execute()
        paginator = StandardResultsSetPagination(request, meeting_types)
        paginated_data = paginator.paginate_queryset()
        serializer = self.serializer_class(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        meeting_type = self.get_meeting_type_service.execute(pk)
        serializer = self.serializer_class(meeting_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        meeting_type = self.update_meeting_type_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(meeting_type).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.delete_meeting_type_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
