from pyexpat import model
from django.shortcuts import render

from .forms import PruebaForm
from .models import Prueba
from django.views.generic import CreateView



# Create your views here.
class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    #fields = ['titulo', 'subtitulo', 'cantidad']
    form_class = PruebaForm
    success_url = '/'
