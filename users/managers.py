from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fileds):
        if not email:
            raise ValueError("Users must have an email addres")
        
        if not password:
            raise ValueError("Users must have a password")
        
        extra_fileds["is_active"] = True 
        
        user = self.model(email=self.normalize_email(email), **extra_fileds)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff, user.is_superuser = True, True
        user.save(using=self._db)
        
        return user
