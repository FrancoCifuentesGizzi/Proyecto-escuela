from re import M
from statistics import mode
from django.contrib.auth.models import AbstractUser
from django.db import models 


class Usuario(AbstractUser):
    rut = models.CharField(max_length=20, unique = True, null=True)
    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Alumno(models.Model):
    rut = models.CharField(max_length=255, primary_key = True)
    nombre = models.CharField(max_length=255,null=True, blank =True)
    apellido = models.CharField(max_length=255, null=True, blank=True)

class Profesor(models.Model):
    rut = models.CharField(max_length=255, primary_key = True)
    nombre = models.CharField(max_length=255,null=True, blank =True)
    apellido = models.CharField(max_length=255, null=True, blank=True)
   
    def __str__(self):
        return self.nombre
class Curso(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    cantidad_alumnos = models.PositiveBigIntegerField(null=True)


class Jefatura(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    profe_jefe = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)

