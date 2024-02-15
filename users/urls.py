from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("sign_up/", views.SignUp.as_view(), name="sign_up_api"),
]
