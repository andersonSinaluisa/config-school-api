from rest_framework.viewsets import ViewSet

from core.application.serializers.section_serializer import SectionSerializer
from core.container import Container
from rest_framework.response import Response
from rest_framework import status

class SectionViewSet(ViewSet):
    """
    A viewset for managing sections.
    """
    serializer_class = SectionSerializer
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_section_service = Container.list_section_service()
        self.retrieve_section_service = Container.get_section_service()
        self.create_section_service = Container.create_section_service()
        self.update_section_service = Container.update_section_service()
        self.delete_section_service = Container.delete_section_service()
    def list(self, request):
        """
        List all sections.
        """
        sections = self.list_section_service.execute()
        serializer = self.serializer_class(sections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific section by ID.
        """
        section = self.retrieve_section_service.execute(pk)

        serializer = self.serializer_class(section)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new section.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            section = self.create_section_service.execute(**serializer.validated_data)
            return Response(self.serializer_class(section).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        """
        Update an existing section.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        section = self.update_section_service.execute(pk, **serializer.validated_data)
        return Response(self.serializer_class(section).data)

    def destroy(self, request, pk=None):
        """
        Delete a section.
        """
        self.delete_section_service.execute(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)