from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from . import managers


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, null=False)
    full_name = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True, null=False)
    is_staff = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    
    objects = managers.UserManager
    
    USERNAME_FIELD = "email"
    
    def __str__(self) -> str:
        return self.full_name
