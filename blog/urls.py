from rest_framework import routers
from django.urls import path, include
from blog.views import BlogView, CommentView, CommentDetailView


app_name = 'blog'


router = routers.DefaultRouter()
router.register('posts', BlogView)


urlpatterns = [
    path('', include(router.urls)),
    path('post/<uuid:post_id>/comments', CommentView.as_view()),
    path('post/<uuid:post_id>/comments/<uuid:comment_id>', CommentDetailView.as_view())
]
