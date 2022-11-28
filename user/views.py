from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        Для регистрации нового пользователя: /api/users/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
