from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'empleados_app'

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path(
        'listar_empleados/', 
        ListAllEmpleados.as_view(), 
        name='all_empleados'
    ),
    path(
        'listar_empleados_admin/', 
        ListAllEmpleadosAdmin.as_view(), 
        name='all_empleados_admin'
    ),
    path(
        'listar_empleados_dpto/<shortname>/', 
        ListByDpto.as_view(),
        name='departamento_empleados'),
    path('listar_empleados_puesto/<elpuesto>/', ListByPuesto.as_view()),
    path('buscar_empleado/', ListBuscarEmpleado.as_view()),
    path('habilidades-empleado/<int:id>/', ListHabilidades.as_view()),
    path(
        'detalle-empleado/<pk>/', 
        EmpleadoDetailView.as_view(),
        name='empleado_detail'),
    path(
        'registrar-empleado/', 
        EmpleadoCreateView.as_view(),
        name='crear'
        ),
    path('success/', SuccessView.as_view(), name='correcto'),
    path(
        'update-empleado/<pk>/', 
        EmpleadoUpdateView.as_view(), 
        name='actualizar'
    ),
    path(
        'delete-empleado/<pk>/', 
        EmpleadoDeleteView.as_view(), 
        name='eliminar'
    ),
]