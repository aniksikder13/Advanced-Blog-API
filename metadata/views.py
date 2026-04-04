from rest_framework import viewsets, permissions
from metadata.serializers import CategrySerializer, TagSerializer
from core.models import Tag, Category


class CategryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
