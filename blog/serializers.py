from core.models import Post, Comment
from rest_framework import serializers
from user.serializers import UserMetaSerializer
from blog_metadata.serializers import CategrySerializer, TagSerializer


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'created_at', 'author', 'category', 'tags']
        read_only_fields = ['id']


class BlogDetailSerializer(BlogSerializer):
    class Meta(BlogSerializer.Meta):
        fields = BlogSerializer.Meta.fields + ['content']


class CommentSerializer(serializers.ModelSerializer):
    user = UserMetaSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'post', 'user']
        read_only_fields = ['id', 'user', 'post']
