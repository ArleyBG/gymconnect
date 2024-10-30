from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from mainapp.models import Administrador, Empleado
from .forms import RegisterEmployee
from django.contrib import messages

# Create your views here.
def home(request):
    user_data = None
    search = False
    
    if request.method == 'GET':
        
        form = request.GET
        
        if 'asistencia' in form:
            name = form.get('asistencia')
            search = True
            try:
                user = Administrador.objects.get(name=name)
            except Administrador.DoesNotExist:
                user_data = None
            else:
                user_data = {
                    'id': user.id,
                    'Nombre': user.name,
                    'CC': user.identification,
                    'Correo': user.email,
                    'Genero': user.gender,
                    'Cumpleaños': user.date_birth,
                    'Celular': user.phone
                }
                
    
    return render(request, 'home/inicio.html', {
        'title': 'Inicio',
        'home': 'Hola',
        'user_data': user_data,
        'search': search
    })
    
def register_huella(request):
    user_data = None
    search = False
    
    if request.method == 'GET':
        búsqueda = request.GET.get('buscar', '').strip()
        
        if búsqueda:
            search = True
            try:
                user = Administrador.objects.get(name=búsqueda)
                user_data = {
                    'id': user.id,
                    'Nombre': user.name,
                    'CC': user.identification,
                    'Correo': user.email,
                    'Genero': user.gender,
                    'Cumpleaños': user.date_birth,
                    'Celular': user.phone
                }
            except Administrador.DoesNotExist:
                user_data = None
    
    return render(request, 'home/registro_huella.html', {
        'title': 'Registro de huella',
        'user_data': user_data,
        'search': search,
    })
    
def empleado(request):
    
    if request.method == 'POST':
        form = RegisterEmployee(request.POST)
        
        if form.is_valid():
            empleado = Empleado(
                type_id = form.cleaned_data['type_id'],
                identification = form.cleaned_data['identification'],
                name = form.cleaned_data['name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                gender = form.cleaned_data['gender'],
                date_birth = form.cleaned_data['date_birth'],
                occupation = form.cleaned_data['occupation'],
                payment = form.cleaned_data['payment'],
                phone = form.cleaned_data['phone'],
                password = form.cleaned_data['password']
            )
            empleado.save()
            messages.success(request, 'Usuario registrado')
            
            return redirect('empleado')
        else:
            print('Por favor corrige los errores en el formulario')
    else:
        form = RegisterEmployee()
    
    return render(request, 'home/empleados.html', {
        'title': 'Empleados',
        'form': form
    }) 
    
def buscar_empleado(request):
    user_data = None
    search_performed = False
    
    if request.method == 'GET':
        búsqueda = request.GET.get('buscar_empleado', '').strip()
        
        if búsqueda:
            search_performed = True
            try:
                user = Empleado.objects.get(name=búsqueda)
                user_data = {
                    'id': user.id,
                    'name': user.name,
                    'last_name': user.last_name,
                    'identification': user.identification,
                    'email': user.email,
                    'gender': user.gender,
                    'date_birth': user.date_birth,
                    'occupation': user.occupation,
                    'payment': user.payment,
                    'phone': user.phone,
                }
                print(f"User ID: {user.id}")
                
            except Empleado.DoesNotExist:
                user_data = None
                
    return render(request, 'home/empleados.html', {
        'user_data': user_data,
        'search_performed': search_performed
    })
    
def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
        
    empleado.delete()
    messages.success(request, 'Empleado eliminado')
    return redirect('empleado')

def cliente(request):
    # Crear una función para buscar un cliente
    # Crear el modelo y el formulario para el cliente
    
    return render(request, 'home/datos_cliente.html', {
        'title': 'Clientes',
    })

def asistencia(request):
    # Función para mostrar la lista de asistencia
    
    return render(request, 'home/inicio.html', {
        'title': 'Asistencia'
    })


                
                