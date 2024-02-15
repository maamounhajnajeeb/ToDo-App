from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request

from . import models, serializers

from utils.permissions import not_authenticated


class SignUp(generics.CreateAPIView):
    queryset = models.User.objects
    serializer_class = serializers.SignUpSerializer
    permission_classes = (not_authenticated.NotAuthenticated, )
    
    def create(self, request: Request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
