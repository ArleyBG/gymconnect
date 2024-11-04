# Importar el formato del formulario
import datetime
import decimal
from django import forms
# Importar la librería de validaciones
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import datetime
from mainapp.models import Empleado
from django.contrib.auth.hashers import make_password
from mainapp.models import Cliente

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
    
class RegisterClient(forms.Form):
    
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
        
        if Cliente.objects.filter(identification=identification).exists():
            raise ValidationError('Ya existe un usuario con este numero de identificación')
        
        return identification
    
    def clean_email(self):
        
        email = self.cleaned_data.get('email')
        
        if Cliente.objects.filter(email=email).exists():
            raise ValidationError('Ya existe un usuario con este correo electrónico')
        
        return email
    
class EvolucionForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
        max_length=100,
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
    
    identification = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su número de identificación'
            }
        ),
        label='ID del Cliente'
    )
    
    date_register = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        ),
        label='Fecha de Evaluación'
    )
    
    peso_corporal = forms.DecimalField(
        label='Peso',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese su peso en kilogramos',
                'class': 'form-control'
            }
        )
    )
    
    imc = forms.DecimalField(
        label='Indice de Masa Corporal',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese su indice de masa corporal',
                'class': 'form-control'
            }
        )
    )
    
    porcentaje_grasa = forms.DecimalField(
        label='Grasa Corporal',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese su porcentaje de grasa corporal',
                'class': 'form-control'
            }
        )
    )
    
    porcentaje_musculo = forms.DecimalField(
        label='Masa Muscular',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese su masa muscular en kilogramos',
                'class': 'form-control'
            }
        )
    )
    
    porcentaje_agua = forms.DecimalField(
        label='Porcentaje de Agua',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese su porcentaje de agua corporal',
                'class': 'form-control'
            }
        )
    )
    
    estatura = forms.DecimalField(
        label='Estatura',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese su altura en metros',
                'class': 'form-control'
            }
        )
    )
    
    hombros = forms.DecimalField(
        label='Medida de Hombros',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese la medida de sus hombros en centímetros',
                'class': 'form-control'
            }
        )
    )
    
    pectoral = forms.DecimalField(
        label='Medida de Pectoral',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese la medida de su pectoral en centímetros',
                'class': 'form-control'
            }
        )
    )
    
    biceps = forms.DecimalField(
        label='Medida de Biceps',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese la medida de su biceps en centímetros',
                'class': 'form-control'
            }
        )
    )
    
    espalda = forms.DecimalField(
        label='Medida de Espalda',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese la medida de su espalda en centímetros',
                'class': 'form-control'
            }
        )
    )
    
    cadera = forms.DecimalField(
        label='Medida de Cadera',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese la medida de su cadera en centímetros',
                'class': 'form-control'
            }
        )
    )
    
    cintura = forms.DecimalField(
        label='Medida de Cintura',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese la medida de su cintura en centímetros',
                'class': 'form-control'
            }
        )
    )
    
    gluteos = forms.DecimalField(
        label='Medida de Gluteos',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese la medida de sus gluteos en centímetros',
                'class': 'form-control'
            }
        )
    )
    
    pierna = forms.DecimalField(
        label='Medida de Piernas',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese la medida de sus piernas en centímetros',
                'class': 'form-control'
            }   
        )
    )
    
    pantorrilla = forms.DecimalField(
        label='Medida de Pantorrillas',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Ingrese la medida de sus pantorrillas en centímetros',
                'class': 'form-control'
            }
        )
    )
    
    def clean_peso_corporal(self):
        peso_corporal = self.cleaned_data.get('peso_corporal')
        if peso_corporal is not None:
            try:
                peso_corporal = round(peso_corporal, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para el peso corporal')
        return peso_corporal

    def clean_imc(self):
        imc = self.cleaned_data.get('imc')
        if imc is not None:
            try:
                imc = round(imc, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para el índice de masa corporal')
        return imc

    def clean_porcentaje_grasa(self):
        porcentaje_grasa = self.cleaned_data.get('porcentaje_grasa')
        if porcentaje_grasa is not None:
            try:
                porcentaje_grasa = round(porcentaje_grasa, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para el porcentaje de grasa corporal')
        return porcentaje_grasa

    def clean_porcentaje_musculo(self):
        porcentaje_musculo = self.cleaned_data.get('porcentaje_musculo')
        if porcentaje_musculo is not None:
            try:
                porcentaje_musculo = round(porcentaje_musculo, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la masa muscular')
        return porcentaje_musculo

    def clean_porcentaje_agua(self):
        porcentaje_agua = self.cleaned_data.get('porcentaje_agua')
        if porcentaje_agua is not None:
            try:
                porcentaje_agua = round(porcentaje_agua, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para el porcentaje de agua corporal')
        return porcentaje_agua

    def clean_estatura(self):
        estatura = self.cleaned_data.get('estatura')
        if estatura is not None:
            try:
                estatura = round(estatura, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la estatura')
        return estatura

    def clean_hombros(self):
        hombros = self.cleaned_data.get('hombros')
        if hombros is not None:
            try:
                hombros = round(hombros, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la medida de hombros')
        return hombros

    def clean_pectoral(self):
        pectoral = self.cleaned_data.get('pectoral')
        if pectoral is not None:
            try:
                pectoral = round(pectoral, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la medida de pectoral')
        return pectoral

    def clean_biceps(self):
        biceps = self.cleaned_data.get('biceps')
        if biceps is not None:
            try:
                biceps = round(biceps, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la medida de biceps')
        return biceps

    def clean_espalda(self):
        espalda = self.cleaned_data.get('espalda')
        if espalda is not None:
            try:
                espalda = round(espalda, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la medida de espalda')
        return espalda

    def clean_cadera(self):
        cadera = self.cleaned_data.get('cadera')
        if cadera is not None:
            try:
                cadera = round(cadera, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la medida de cadera')
        return cadera

    def clean_cintura(self):
        cintura = self.cleaned_data.get('cintura')
        if cintura is not None:
            try:
                cintura = round(cintura, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la medida de cintura')
        return cintura

    def clean_gluteos(self):
        gluteos = self.cleaned_data.get('gluteos')
        if gluteos is not None:
            try:
                gluteos = round(gluteos, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la medida de gluteos')
        return gluteos

    def clean_pierna(self):
        pierna = self.cleaned_data.get('pierna')
        if pierna is not None:
            try:
                pierna = round(pierna, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la medida de piernas')
        return pierna

    def clean_pantorrilla(self):
        pantorrilla = self.cleaned_data.get('pantorrilla')
        if pantorrilla is not None:
            try:
                pantorrilla = round(pantorrilla, 2)
            except decimal.InvalidOperation:
                raise ValidationError('Ingrese un valor válido para la medida de pantorrillas')
        return pantorrilla

    def clean_date_register(self):
        date_register = self.cleaned_data.get('date_register')
        
        if date_register > datetime.date.today():
            raise ValidationError('La fecha de evaluación no puede ser mayor a la fecha actual')
        
        return date_register        
    
class ReservaForm(forms.Form):
    identification = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su número de identificación'
            }
        ),
        label='ID del Cliente'
    )
    
    name = forms.CharField(
        label = 'Nombre',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre completo'
            }
        )
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su correo electrónico'
            }
        )
    )
    
    type_reserve = forms.ChoiceField(
        choices=[
            ('E', 'Entrenamiento Personal'),
            ('M', 'Membresía'),
            ('S', 'Spa')
        ],
        label='Tipo de Reserva',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seleccione el tipo de reserva'
            }
        )
    )
    
    date_reserve = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        ),
        label='Fecha de Reserva'
    )
    
    time_reserve = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control'
            }
        ),
        label='Hora de Reserva'
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
    
    def clean_date_register(self):
        date_register = self.cleaned_data.get('date_register')
        
        if date_register < datetime.date.today():
            raise ValidationError('La fecha de reserva no puede ser menor a la fecha actual')
        
        return date_register