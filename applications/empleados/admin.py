from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

#Personalizar el administrador de Django
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job',
        'departamento',
        'full_name',
        'id',
    )

    def full_name(self, obj): #forma de declarar un función para ej. columna adicional
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name', ) #lista o tupla
    list_filter = ['job', 'habilidades'] #lista o tupla
    # en las relaciones de muchos a muchos, para que aparezca un filtro horizontal al registrar las habilidades de los empleados
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)