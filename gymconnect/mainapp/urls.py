from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.register_admin, name="administrador"),
    path('login/', views.login_admin, name='login'),
]
