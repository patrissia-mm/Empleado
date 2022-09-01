from multiprocessing import context
from django.urls import reverse_lazy
from pydoc import pager
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado
from .forms import EmpleadoForm

""" Vista para cargar la página de inicio """
class InicioView(TemplateView):
    template_name = 'inicio.html'

""" **************************** ListView ****************************"""
#1. Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    #model = Empleado   #al usar un query set abajo, ya no es necesario
    context_object_name = 'empleados'
    #Para trabajar con paginación
    paginate_by = 4
    ordering = 'first_name'

    #añadimos esta función para listar empleados buscados en base a la palabra de la caja de texto de un formulario o una variable get enviada
    def get_queryset(self):
        #Obtener la palabra que fue introducida en el textbox kword y enviada por el formulario mediante el método GET
        palabra_clave=self.request.GET.get("kword","")
        lista=Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


#1.1 Listar todos los empleados de la empresa
class ListAllEmpleadosAdmin(ListView):
    template_name = 'empleados/list_all_admin.html'
    model = Empleado 
    context_object_name = 'empleados'
    #Para trabajar con paginación
    paginate_by = 6
    ordering = 'first_name'


#2. Listar los empleados de un departamento
class ListByDpto(ListView):
    template_name = 'empleados/list_by_dpto.html'
    context_object_name = 'empleados'
    """queryset = Empleado.objects.filter(
        departamento__short_name = 'Bienestar'
    )"""
    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista

#3. Listar empleados por trabajo
class ListByPuesto(ListView):
    template_name   ='empleados/list_by_puesto.html'
    def get_queryset(self):
        puesto = self.kwargs['elpuesto']
        lista = Empleado.objects.filter(
            job = puesto
        )
        return lista

#4 Buscar empleado x nombre
class ListBuscarEmpleado(ListView):
    template_name = 'empleados/buscar_empleado.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        #Obtener la palabra que fue introducida en el textbox kword y enviada por el formulario mediante el método GET
        palabra_clave=self.request.GET.get("kword","")
        lista=Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

#5. Listar habilidades de un empleado
class ListHabilidades(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'
    def get_queryset(self):
        id_empleado = self.kwargs['id']
        empleado = Empleado.objects.get(id=id_empleado)
        return empleado.habilidades.all()

""" **************************** DetailView ****************************"""

# Ver todo el registro de un modelo empleado
class EmpleadoDetailView(DetailView):
    template_name = "empleados/detail_empleado.html"
    model = Empleado

    # ejemplo de cómo añadir un campo que no es parte del modelo
    def get_context_data(self, **kwargs):
        context=super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context

""" **************************** CreateView ****************************"""
# clase tipo Template paramostrar una página de éxito
class SuccessView(TemplateView):
    template_name = "empleados/success.html"

#Reagistrar un empleado
class EmpleadoCreateView(CreateView):
    model           = Empleado
    template_name   = "empleados/add.html"
    #listar todos los campos en el formulario
    #fields          = ('__all__') 
    #listar sólo algunos campos
    #Se usa cuando no se usa el ModelForm, sólo el Modelo por defecto
    """ fields=[
        'first_name', 
        'last_name', 
        'job', 
        'departamento', 
        'habilidades',
        'avatar'
    ] """
    #Para cuando se usa el forms.py con el ModelForm
    form_class  = EmpleadoForm
    #*****Se redigirá a la misma pagina al realizar con éxito el registro
    #success_url     = '.' 
    #*****Se redigirá a una nueva página, representaada en urls.py con el siguiente nombre
    success_url = reverse_lazy('empleados_app:all_empleados')

    # Ejemplo de uso del Método form_valid para interceptar datos que se estan almacenando
    def form_valid(self, form):
        #lógica del proceso de almacenar un dato full_name creado por la suma de 2 campos de la base de datos
        emp = form.save()
        emp.full_name = emp.first_name + ' ' + emp.last_name
        emp.save()
        return super(EmpleadoCreateView, self).form_valid(form)


""" **************************** UpdateView ****************************"""
class EmpleadoUpdateView(UpdateView):
    template_name   = 'empleados/update_empleado.html'
    model           = Empleado
    fields          = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url     = reverse_lazy('empleados_app:all_empleados_admin')

    #Ejemplo del uso del método de un UpdateView, para interceptar datos que se están guardando
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('******************* MÉTODO POST ************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

""" **************************** DeleteView ****************************"""    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/eliminar_empleado.html"
    success_url = reverse_lazy('empleados_app:all_empleados_admin')

