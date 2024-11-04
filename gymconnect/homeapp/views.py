from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from mainapp.models import Administrador, Empleado, Cliente, Evolucion, Reserva
from .forms import RegisterEmployee, RegisterClient, EvolucionForm, ReservaForm
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
        'form': RegisterEmployee(),
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
    if request.method == 'POST':
        form = RegisterClient(request.POST)
        
        if form.is_valid():
            cliente = Cliente(
                type_id = form.cleaned_data['type_id'],
                identification = form.cleaned_data['identification'],
                name = form.cleaned_data['name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                gender = form.cleaned_data['gender'],
                date_birth = form.cleaned_data['date_birth'],
                phone = form.cleaned_data['phone'],
                password = form.cleaned_data['password']
            )
            cliente.save()
            messages.success(request, 'Cliente registrado')
            
            return redirect('cliente')
        else: 
            print('Por favor corrige los errores en el formulario')
    else:
        form = RegisterClient()
    
    return render(request, 'home/datos_cliente.html', {
        'title': 'Clientes',
        'form': form,
    })
    
def buscar_cliente(request):
    user_data = None
    search_performed = False
    
    if request.method == 'GET':
        búsqueda = request.GET.get('buscar_cliente', '').strip()
        
        if búsqueda:
            search_performed = True
            try:
                user = Cliente.objects.get(name=búsqueda)
                user_data = {
                    'id': user.id,
                    'name': user.name,
                    'last_name': user.last_name,
                    'identification': user.identification,
                    'email': user.email,
                    'gender': user.gender,
                    'date_birth': user.date_birth,
                    'phone': user.phone,
                }
                print(f"User ID: {user.id}")
                
            except Cliente.DoesNotExist:
                user_data = None
                
    return render(request, 'home/datos_cliente.html', {
        'title': 'Clientes',
        'form': RegisterClient(),
        'user_data': user_data,
        'search_performed': search_performed
    })

def asistencia(request):
    # Función para mostrar la lista de asistencia
    
    return render(request, 'home/inicio.html', {
        'title': 'Asistencia'
    })

def show_clients(request):
    # Función para mostrar la lista de clientes
    clients = Cliente.objects.all()
    
    return render(request, 'home/list_client.html', {
        'title': 'Lista de clientes',
        'clients': clients
    })
    
    
def evolucion(request):
    # Función para guardar la evolución de un cliente
    
    if request.method == 'POST':
        form = EvolucionForm(request.POST)
        
        if form.is_valid():
            try:
                cliente = Cliente.objects.get(
                    name=form.cleaned_data['name'], 
                    identification=form.cleaned_data['identification']
                )
            except Cliente.DoesNotExist:
                messages.error(request, 'Cliente no encontrado')
                return redirect('evolucion')
            
            evolucion = Evolucion(
                cliente=cliente,
                name=form.cleaned_data['name'],
                identification=form.cleaned_data['identification'],
                date_register=form.cleaned_data['date_register'],
                peso_corporal=form.cleaned_data['peso_corporal'],
                estatura=form.cleaned_data['estatura'],
                imc=form.cleaned_data['imc'],
                porcentaje_grasa=form.cleaned_data['porcentaje_grasa'],
                porcentaje_musculo=form.cleaned_data['porcentaje_musculo'],
                porcentaje_agua=form.cleaned_data['porcentaje_agua'],
                hombros=form.cleaned_data['hombros'],
                pectoral=form.cleaned_data['pectoral'],
                biceps=form.cleaned_data['biceps'],
                espalda=form.cleaned_data['espalda'],
                cintura=form.cleaned_data['cintura'],
                cadera=form.cleaned_data['cadera'],
                gluteos=form.cleaned_data['gluteos'],
                pierna=form.cleaned_data['pierna'],
                pantorrilla=form.cleaned_data['pantorrilla'],
            )
            evolucion.save()
            messages.success(request, 'Registro de evolución guardado')
            return redirect('evolucion')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = EvolucionForm()
        
    return render(request, 'home/evolucion.html', {
        'title': 'Evolución',
        'form': form
    })

def search_evolucion(request):
    # Función para buscar la evolución de un cliente
    user_data = None
    search_performed = False
    
    if request.method == 'GET':
        búsqueda = request.GET.get('buscar_evolucion', '').strip()
        
        if búsqueda:
            search_performed = True
            try:
                user = Evolucion.objects.get(name=búsqueda)
                user_data = {
                    'name': user.name,
                    'date_register': user.date_register,
                    'peso_corporal': user.peso_corporal,
                    'estatura': user.estatura,
                    'imc': user.imc,
                    'porcentaje_grasa': user.porcentaje_grasa,
                    'porcentaje_musculo': user.porcentaje_musculo,
                    'porcentaje_agua': user.porcentaje_agua,
                    'hombros': user.hombros,
                    'pectoral': user.pectoral,
                    'biceps': user.biceps,
                    'espalda': user.espalda,
                    'cintura': user.cintura,
                    'cadera': user.cadera,
                    'gluteos': user.gluteos,
                    'pierna': user.pierna,
                    'pantorrilla': user.pantorrilla,
                }
                print(f"User ID: {user.name}")
                
            except Cliente.DoesNotExist:
                user_data = None
                
    return render(request, 'home/evolucion.html', {
        'title': 'Evolución',
        'form': EvolucionForm(),
        'user_data': user_data,
        'search_performed': search_performed
    })
    
def reservaciones(request):
    # Función para mostrar las reservaciones de los clientes
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        
        if form.is_valid():
            administrador = Administrador.objects.first()  # Replace with appropriate logic to get the correct administrador
            try:
                cliente = Cliente.objects.get(identification=form.cleaned_data['identification'])
            except Cliente.DoesNotExist:
                messages.error(request, 'Cliente no encontrado')
                return redirect('reservaciones')
            
            reserva = Reserva(
                cliente = cliente,
                identification = form.cleaned_data['identification'],
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                type_reserve = form.cleaned_data['type_reserve'],
                date_reserve = form.cleaned_data['date_reserve'],
                time_reserve = form.cleaned_data['time_reserve'],
                phone = form.cleaned_data['phone'],
                administrador = administrador
            )
            reserva.save()
            messages.success(request, 'Reservación guardada')
            return redirect('reservaciones')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = ReservaForm()
        
    return render(request, 'home/reservaciones.html', {
        'title': 'Reservaciones',
        'form': form
    })
    
def buscar_reserva(request):
    user_data = None
    search = False
    
    if request.method == 'GET':
        buscar = request.GET.get('buscar_reserva', '').strip()
        
        if buscar:
            search = True
            try:
                reserva = Reserva.objects.get(name=buscar)
                user_data = {
                    'name': reserva.name,
                    'identification': reserva.identification,
                    'email': reserva.email,
                    'type_reserve': reserva.type_reserve,
                    'date_reserve': reserva.date_reserve,
                    'time_reserve': reserva.time_reserve,
                    'phone': reserva.phone
                }
                print(f"User ID: {reserva.name}")
                
            except Reserva.DoesNotExist:
                user_data = None
                
    return render(request, 'home/reservaciones.html', {
        'title': 'Reservaciones',
        'form': ReservaForm(),
        'user_data': user_data,
        'search': search
    })
                
                
                