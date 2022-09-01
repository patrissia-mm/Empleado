from multiprocessing.dummy import JoinableQueue
from django.db import models

from applications.departamento.models import Departamento

# Create your models here.

# Modelo para la tabla habilidades
class Habilidades(models.Model):
    habilidad   =models.CharField('Habilidades', max_length=50)
    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades Empleado'
    def __str__(self):
        return str(self.id) + '-' + self.habilidad



#""" Modelo para la tabla empleado """
class Empleado(models.Model):
    job_choises=(
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'SECRETARIA'),
        ('3', 'OTRO')
    )
    first_name   =models.CharField('Nombres', max_length=50)
    last_name   =models.CharField('Apellidos', max_length=50)
    full_name   =models.CharField('Nombre Completo', max_length=100, blank=True)
    job         =models.CharField('Puesto', max_length=1, choices=job_choises)
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar      =models.ImageField(upload_to='empleado', blank=True, null=True)
    #Relación muchos a muchos con habilidades
    habilidades =models.ManyToManyField(Habilidades)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Mis Empleados'
        ordering = ['last_name']
        unique_together=('last_name', 'first_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name    