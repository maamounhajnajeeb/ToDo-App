from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

from rest_framework import generics, decorators
from rest_framework import permissions, views
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView

from . import models, serializers

from utils.permissions import not_authenticated, owner_only

Users = get_user_model()


class SignUp(generics.CreateAPIView):
    queryset = models.User.objects
    serializer_class = serializers.SignUpSerializer
    permission_classes = (not_authenticated.NotAuthenticated, )
    
    def create(self, request: Request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class LogIn(TokenObtainPairView):
    serializer_class = serializers.LogInSerializer
    permission_classes = (not_authenticated.NotAuthenticated, )


@decorators.api_view(["POST", ])
def validate_password(req: Request):
    password = req.data.get("password")
    if not password:
        return Response({"Error": "Password field needed"}, status=status.HTTP_400_BAD_REQUEST)
    
    checking = check_password(password, req.user.password)
    if checking == True:
        return Response({"Success": "The password is right, you can change it now"}
                , status=status.HTTP_202_ACCEPTED)
    
    return Response({"Error": "Not same user password"}, status=status.HTTP_406_NOT_ACCEPTABLE)


class NewPassword(views.APIView):
    def post(self, request: Request, format=None):
        serializer = serializers.NewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        new_password = serializer.data.get("password")
        user = request.user
        user.change_password(new_password)
        
        return Response({"Success": "Password changed successfully"}, status=status.HTTP_202_ACCEPTED)


class Users(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, owner_only.IsOwner, )
    serializer_class = serializers.UserSerializer
    queryset = Users.objects
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
