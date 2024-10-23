# Importar el formato del formulario
from django import forms
# Importar la librería de validaciones
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from mainapp.models import Empleado
from django.contrib.auth.hashers import make_password

class RegisterEmployee(forms.Form):
    
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
    
    identification = forms.CharField(
        label='Numero de Documento',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese su numero de  documento',
                'class': 'form-control'
            }
        )
    )
    
    name = forms.CharField(
        label='Nombre',
        max_length=100, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese su Nombre completo',
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
    
    last_name = forms.CharField(
        label='Apellidos',
        max_length=100, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese su apellido completo',
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
            attrs={
                'type':'date',
                'class': 'form-control'
            }),
            label='Fecha de Nacimiento'
    )
    
    occupation = forms.CharField(
        label='Ocupación',
        max_length=100,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el cargo del empleado',
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
    
    payment = forms.DecimalField(
        label='Sueldo',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese el salario en números',
                'class': 'form-control'
            }
        )
    )
    
    phone = forms.CharField(
        label='Numero de Celular',
        widget=forms.TextInput(
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
        
        if Empleado.objects.filter(identification=identification).exists():
            raise ValidationError('Ya existe un usuario con este numero de identificación')
        
        return identification
    
    def clean_email(self):
        
        email = self.cleaned_data.get('email')
        
        if Empleado.objects.filter(email=email).exists():
            raise ValidationError('Ya existe un usuario con este correo electrónico')
        
        return email