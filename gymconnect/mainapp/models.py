from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Administrador(AbstractBaseUser):
    TIPO_ID_CHOICES = [
        ('TI', 'Tipo de identificación'),
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('PA', 'Pasaporte')
    ]
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
 
    id = models.AutoField(primary_key=True)
    type_id = models.CharField(max_length=20, choices=TIPO_ID_CHOICES)
    identification = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20, choices=SEXO_CHOICES)
    date_birth = models.DateField()
    phone = models.IntegerField()
    password = models.CharField(max_length=100)
    
    REQUIRED_FIELDS = ['']
    USERNAME_FIELD = 'email'
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.name
    
class Empleado(models.Model):
    TIPO_ID_CHOICES = [
    ('TI', 'Tipo de identificación'),
    ('CC', 'Cédula de ciudadanía'),
    ('CE', 'Cédula de extranjería'),
    ('PA', 'Pasaporte')
    ]
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
    
    id = models.AutoField(primary_key=True)
    type_id = models.CharField(max_length=10, choices=TIPO_ID_CHOICES)
    identification = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=SEXO_CHOICES)
    date_register = models.DateField(auto_now_add=True)
    date_birth = models.DateField()
    occupation = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    password = models.CharField(max_length=100)
    administrador = models.ForeignKey(Administrador, null=True, on_delete=models.CASCADE, related_name='empleados')

    
    def __str__(self):
        return f"{self.name} {self.last_name}"
    