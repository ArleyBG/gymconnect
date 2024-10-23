from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.home, name='inicio'),
    path('empleado/', views.empleado, name='empleado'),
    path('buscar_empleado/', views.buscar_empleado, name="buscar_empleado"),
    path('eliminar_empleado/<int:id>/', views.eliminar_empleado, name="eliminar_empleado"),
]
