from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from mainapp.forms import RegisterForm, LoginForm
from django.contrib import messages
from .models import Administrador
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from mainapp.forms import RegisterForm, LoginForm
from django.contrib import messages
from .models import Administrador
import googlemaps
import json
from pprint import pprint
import time


# Create your views here.
def index(request):
    
    """
    if request.method == 'GET':
        query = request.GET.get('ciudad')
        gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        places = gmaps.places(query, type='location')
        
        next_page_token = places.get("next_page_token")

        # Esperar un poco antes de solicitar la siguiente página
        time.sleep(2)

        # Obtener la siguiente página de resultados
        next_page_places = gmaps.places(query, type='location', page_token=next_page_token)
        """
    
    return render(request, 'mainapp/index.html', {
        'title': 'Gymconnect'
    })
    
def register_admin(request):
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            administrador = Administrador(
                type_id=register_form.cleaned_data['type_id'],
                identification=register_form.cleaned_data['identification'],
                name=register_form.cleaned_data['name'],
                email=register_form.cleaned_data['email'],
                gender=register_form.cleaned_data['gender'],
                date_birth=register_form.cleaned_data['date_birth'],
                phone=register_form.cleaned_data['phone'],
                password=register_form.cleaned_data['password']
            )
            
            administrador.save()
            messages.success(request, '¡Te has registrado con éxito!')
            
            return redirect('inicio')
        else:
            print('Por favor corrige los errores en el formulario')
    else:
        register_form = RegisterForm()
    
    return render(request, 'users/register-admin.html', {
        'title': 'Crea un usuario para continuar',
        'register_form': register_form
    })
    
def login_admin(request):
    
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                
                return redirect('inicio')
            
            else:
                messages.warning(request, 'Nombre de usuario o contraseña incorrectos')
        else:
            messages.warning(request, 'Formulario no valido. Verifica los campos')
    else:
        login_form = LoginForm()
        
    return render(request, 'users/login-admin.html', {
        'title': 'Iniciar sesión',
        'user': 'Administrador',
        'login_form': login_form
    })

