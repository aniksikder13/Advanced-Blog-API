from rest_framework import serializers
from core.models import Category, Tag


class BaseNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']
        read_only_fields = ['id']


class TagSerializer(BaseNameSerializer):
    class Meta(BaseNameSerializer.Meta):
        model = Tag


class CategrySerializer(BaseNameSerializer):
    class Meta(BaseNameSerializer.Meta):
        fields = TagSerializer.Meta.fields + ['description']
        model = Category
