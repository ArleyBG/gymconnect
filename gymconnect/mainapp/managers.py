from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        # Crea un usuario personalizado
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        
        # Crea un superusuario personalizado
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
