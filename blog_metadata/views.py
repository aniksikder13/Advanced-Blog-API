from core.models import Tag, Category
from rest_framework import viewsets, permissions
from blog_metadata.serializers import CategrySerializer, TagSerializer


class CategryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


