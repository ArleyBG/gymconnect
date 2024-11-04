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
    
class Cliente(models.Model):
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
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    administrador = models.ForeignKey(Administrador, null=True, on_delete=models.CASCADE, related_name='clientes')

    
    def __str__(self):
        return f"{self.name} {self.last_name}"
    
class Evolucion(models.Model):
    name = models.CharField(max_length=50)
    identification = models.CharField(max_length=20)
    date_register = models.DateField(auto_now_add=True)
    peso_corporal = models.DecimalField(max_digits=5, decimal_places=2)
    estatura = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    porcentaje_grasa = models.DecimalField(max_digits=5, decimal_places=2)
    porcentaje_musculo = models.DecimalField(max_digits=5, decimal_places=2)
    porcentaje_agua = models.DecimalField(max_digits=5, decimal_places=2)
    hombros = models.DecimalField(max_digits=5, decimal_places=2)
    pectoral = models.DecimalField(max_digits=5, decimal_places=2)
    biceps = models.DecimalField(max_digits=5, decimal_places=2)
    espalda = models.DecimalField(max_digits=5, decimal_places=2)
    cintura = models.DecimalField(max_digits=5, decimal_places=2)
    cadera = models.DecimalField(max_digits=5, decimal_places=2)
    gluteos = models.DecimalField(max_digits=5, decimal_places=2)
    pierna = models.DecimalField(max_digits=5, decimal_places=2)
    pantorrilla = models.DecimalField(max_digits=5, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='evoluciones')
    
    def __str__(self):
        return f"{self.cliente}"
    
class Reserva(models.Model):
    TIPO_RESERVE_CHOICES = [
        ('E', 'Entrenamiento personal'),
        ('M', 'Membresía'),
        ('S', 'Spa')
    ]
    
    id = models.AutoField(primary_key=True)
    identification = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    type_reserve = models.CharField(max_length=50, choices=TIPO_RESERVE_CHOICES)
    date_register = models.DateField(auto_now_add=True)
    date_reserve = models.DateField()
    time_reserve = models.TimeField()
    phone = models.CharField(max_length=15)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, related_name='reservas')
    
    def __str__(self):
        return f"{self.id}"
    
    
    