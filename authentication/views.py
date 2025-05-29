from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSerializer, RegisterUserSerializer
from .permissions import IsSelfOrAdminOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsSelfOrAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == "create":
            return RegisterUserSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        return super().get_permissions()
