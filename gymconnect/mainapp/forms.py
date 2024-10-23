# Importar el formato del formulario
from django import forms
# Importar la librería de validaciones
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import Administrador
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.Form):
    
    type_id = forms.ChoiceField(
        choices=[
            ('TI', 'Tipo de identificación'), 
            ('CC', 'Cédula de ciudadanía'), 
            ('CE', 'Cédula de extranjería'), 
            ('PA', 'Pasaporte')
        ],
        label='Tipo de Identificación',
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    identification = forms.IntegerField(
        label='Numero de Documento',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese su numero de  documento',
                'class': 'form-control'
            }
        )
    )
    
    name = forms.CharField(
        label='Nombres',
        max_length=100, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese su Nombre y Apellido',
                'class': 'form-control'
            }
        ),
        validators=[
            RegexValidator(
                regex='^[A-Za-z ]+$',
                message='Ingrese solo letras y espacios',
                code='invalid_nombres'
            )
        ]
    )
    
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Ingrese su correo electrónico',
                'class': 'form-control'
            }
        )
    )
    
    gender = forms.ChoiceField(
        choices=[
            ('M', 'Masculino'), 
            ('F', 'Femenino'), 
            ('O', 'Otro')
            ],
        label='Sexo',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    date_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={'type':'date'}),
            label='Fecha de Nacimiento'
    )
    
    phone = forms.IntegerField(
        label='Numero de Celular',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese su numero de celular',
                'class': 'form-control'
            }
        )
    )
    
    password = forms.CharField(
        label='Contraseña',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese su contraseña',
                'class': 'form-control'
            }
        )
    )
    
    def clean_password(self):
        """
        Limpia y convierte la contraseña en formato hash antes de guardarla.
        """
        raw_password = self.cleaned_data.get('password')
        return make_password(raw_password)
    

    def clean_identification(self):
        
        identification = self.cleaned_data.get('identification')
        
        if Administrador.objects.filter(identification=identification).exists():
            raise ValidationError('Ya existe un usuario con este numero de identificación')
        
        return identification
    
    def clean_email(self):
        
        email = self.cleaned_data.get('email')
        
        if Administrador.objects.filter(email=email).exists():
            raise ValidationError('Ya existe un usuario con este correo electrónico')
        
        return email
    
class LoginForm(forms.Form):
    
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Ingrese su correo electrónico',
                'class': 'form-control'
            }
        )
    )
    
    password = forms.CharField(
        label='Contraseña',
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese su contraseña',
                'class': 'form-control'
            }
        )
    )
        
        