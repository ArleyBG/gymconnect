from django.test import TestCase
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.

@pytest.mark.django_db
def test_login_admin(client):
    # Crear un usuario de prueba
    user = User.objects.create_user(
        name='admin', 
        email='admin@example.com', 
        password='adminpassword',
        identification='1123456789',
        date_birth='2024-09-01',
        phone='3177477308'
    )
    
    # Datos de inicio de sesión
    login_data = {
        'email': 'admin@example.com',
        'password': 'adminpassword'
    }
    
    # Realizar la solicitud POST para iniciar sesión
    response = client.post(reverse('login'), login_data)
    
    # Verificar que la redirection sea correcta
    assert response.status_code == 302
    assert response.url == reverse('inicio')
    
    # Verificar que el usuario esté autenticado
    assert '_auth_user_id' in client.session

@pytest.mark.django_db
def test_login_admin_invalid_credentials(client):
    # Datos de inicio de sesión incorrectos
    login_data = {
        'email': 'admin@example.com',
        'password': 'wrongpassword'
    }
    
    # Realizar la solicitud POST para iniciar sesión
    response = client.post(reverse('login'), login_data)
    
    # Verificar que la respuesta sea correcta
    assert response.status_code == 200
    assert 'Nombre de usuario o contraseña incorrectos' in response.content.decode()

