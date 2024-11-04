from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.home, name='inicio'),
    path('empleado/', views.empleado, name='empleado'),
    path('buscar_empleado/', views.buscar_empleado, name="buscar_empleado"),
    path('eliminar_empleado/<int:id>/', views.eliminar_empleado, name="eliminar_empleado"),
    path('registro_huella/', views.register_huella, name='registro_huella'),
    path('cliente/', views.cliente, name='cliente'),
    path('buscar_cliente/', views.buscar_cliente, name="buscar_cliente"),
    path('list_client/', views.show_clients, name="list_client"),
    path('evolucion/', views.evolucion, name='evolucion'),
    path('buscar_evolucion/', views.search_evolucion, name="buscar_evolucion"),
    path('reservaciones/', views.reservaciones, name='reservaciones'),
    path('buscar_reserva/', views.buscar_reserva, name="buscar_reserva"),
]
