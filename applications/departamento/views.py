from django.shortcuts import render
from django.views.generic import ListView
from .forms import NewDepartamentoForm
from django.views.generic.edit import FormView
from applications.empleados.models import Empleado
from .models import Departamento

# Create your views here.

#Vista para listar todos los departamentos
class ListAllDepartamentosView(ListView):
    template_name = 'departamento/lista_departamentos.html'
    model = Departamento
    context_object_name = 'departamentos'


#Vista para crear un departamento, pero creando también un empleado a dicho departamento (registrar en 2 modelos a la vez usando :forms)
class NewDepartamentoView(FormView):
    template_name = 'departamento/add_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        #1ra forma: crear una instancia de departamento y guardar en la DB
        depa=Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname']
        )
        depa.save()

        #2da forma: registrar los datos del empleado interceptando los datos enviados desde el formulario y con la instancia depa ya creada
        nombre = form.cleaned_data['nombre']
        apellidos =form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name  = nombre,
            last_name = apellidos,
            job = '1',
            departamento = depa #Es clave foránea por lo que es un objeto?

        )
        return super(NewDepartamentoView, self).form_valid(form)