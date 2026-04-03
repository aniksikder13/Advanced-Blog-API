from user.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = get_user_model().objects.all()


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        return self.request.user
