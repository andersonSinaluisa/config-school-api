from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from core.application.serializers.level_serializer import LevelSerializer
from core.container import Container


class LevelViewSet(ViewSet):
    """
    A viewset for viewing and editing level instances.
    """
    serializer_class = LevelSerializer
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_level_service = Container.create_level_service()
        self.list_level_service = Container.list_level_service()
        self.get_level_service = Container.get_level_service()
        self.update_level_service = Container.update_level_service()
        self.delete_level_service = Container.delete_level_service()
        
    def create(self, request):
        """
        Create a new level.
        Expects a JSON payload with level details.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        level = self.create_level_service.execute(
            **serializer.validated_data)
        return Response(self.serializer_class(level).data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        """
        List all levels.
        """
        levels = self.list_level_service.execute()
        serializer = self.serializer_class(levels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, pk=None):
        """
        Retrieve a level by its ID.
        """
        level = self.get_level_service.execute(pk)
        if not level:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(level)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def update(self, request, pk=None):
        """
        Update a level by its ID.
        Expects a JSON payload with updated level details.
        """
        level = self.get_level_service.execute(pk)
        if not level:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(level, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_level = self.update_level_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(updated_level).data, status=status.HTTP_200_OK)
    
    
    def destroy(self, request, pk=None):
        """
        Delete a level by its ID.
        """
        level = self.get_level_service.execute(pk)
        if not level:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.delete_level_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    