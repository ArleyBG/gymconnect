from django.contrib.auth.backends import ModelBackend
from .models import Administrador

class CustomBackend(ModelBackend):
    
    def authenticate(self, request, email=None, password=None, **kwargs):
        
        try:
            user = Administrador.objects.get(email=email)
        except Administrador.DoesNotExist:
            return None

        if password and user.check_password(password):
            return user
        
        return None
        
