from django.urls import path
from user.views import UserCreateView, ManageUserView

app_name = 'user'

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('me/', ManageUserView.as_view(), name='me')
]
