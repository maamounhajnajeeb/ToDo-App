from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views

app_name = "users"

urlpatterns = [
    # Users API's
    path("<int:pk>/", views.Users.as_view(), name="users_API's"),
    
    # Authentication
    path("sign_up/", views.SignUp.as_view(), name="sign_up_api"),
    path("sign_in/", views.LogIn.as_view(), name="log_in_api"),
    path("refresh_token/", TokenRefreshView.as_view(), name="referesh_token_api"),
    
    # Change password
    path("validate_current_password/", views.validate_password, name="validate_password"),
    path("new_password/", views.NewPassword.as_view(), name="new_password"),
]
