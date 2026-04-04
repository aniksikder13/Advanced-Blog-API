from django.urls import path, include
from rest_framework import routers
from metadata.views import CategryView, TagView


app_name = 'metadata'


router = routers.DefaultRouter()
router.register('categories', CategryView)
router.register('tags', TagView)


urlpatterns = [
    path('', include(router.urls))
]
