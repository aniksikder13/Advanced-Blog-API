from core.models import Post, Comment
from rest_framework import viewsets, permissions, generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from blog.serializers import BlogSerializer, BlogDetailSerializer, CommentSerializer


class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = Post.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        return serializer.save(user=self.request.user, post=post)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    lookup_field = 'id'           # the model field to filter on
    lookup_url_kwarg = 'comment_id'  # the name in your URL

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')

        return Comment.objects.filter(post=post_id)