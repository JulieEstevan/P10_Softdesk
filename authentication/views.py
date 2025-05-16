from rest_framework import ModelViewSet

from .models import User
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    """
    ViewSet for the User model.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Returns the queryset of users.
        """
        return User.objects.all()
