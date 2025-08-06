from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.api.configuration.pagination import StandardResultsSetPagination
from core.application.serializers.attendance_code_serializer import AttendanceCodeSerializer
from core.container import Container


class AttendanceCodeViewSet(ViewSet):
    """ViewSet for managing attendance codes."""
    serializer_class = AttendanceCodeSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_attendance_code_service = Container.create_attendance_code_service()
        self.delete_attendance_code_service = Container.delete_attendance_code_service()
        self.get_attendance_code_service = Container.get_attendance_code_service()
        self.list_attendance_code_service = Container.list_attendance_code_service()
        self.update_attendance_code_service = Container.update_attendance_code_service()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        attendance_code = self.create_attendance_code_service.execute(**serializer.validated_data)
        return Response(self.serializer_class(attendance_code).data, status=status.HTTP_201_CREATED)

    def list(self, request):
        attendance_codes = self.list_attendance_code_service.execute()
        paginator = StandardResultsSetPagination(request, attendance_codes)
        paginated_data = paginator.paginate_queryset()
        serializer = self.serializer_class(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        attendance_code = self.get_attendance_code_service.execute(pk)
        serializer = self.serializer_class(attendance_code)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        attendance_code = self.update_attendance_code_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(attendance_code).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.delete_attendance_code_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
