from django.urls import path, include
from rest_framework import routers
from blog_metadata.views import CategryView, TagView


app_name = 'blog_metadata'


router = routers.DefaultRouter()
router.register('tags', TagView)
router.register('categories', CategryView)


urlpatterns = [
    path('', include(router.urls))
]
