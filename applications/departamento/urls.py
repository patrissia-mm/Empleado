from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'departamento_app' 

urlpatterns = [
    path('list-departamentos/', ListAllDepartamentosView.as_view(), name='lista_departamentos'),
    path(
        'add-departamento/', 
        NewDepartamentoView.as_view(), 
        name='registrar_departamento'
        ),
]