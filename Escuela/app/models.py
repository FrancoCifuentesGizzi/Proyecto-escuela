
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    username = models.CharField('Rut de usuario: ', primary_key=True, unique=True, max_length=20)
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class ALUMNO(models.Model):
    rut_alumno=models.CharField(primary_key=True, max_length=15)
    nombre_alumno=models.CharField(max_length=100)
    apellido_alumno=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_alumno + ' ' + self.apellido_alumno

class PROFESOR(models.Model):
    rut_profesor = models.CharField(max_length=255, primary_key = True)
    nombre_profesor = models.CharField(max_length=255,null=True, blank =True)
    apellido_profesor = models.CharField(max_length=255, null=True, blank=True)
   
    def __str__(self):
        return self.nombre_profesor + ' ' + self.apellido_profesor

class CURSO(models.Model):
    nivel = models.CharField(max_length=100)
    def __str__(self):
        return self.nivel

class CURSA(models.Model):
    year = models.DateField()
    ALUMNO = models.ForeignKey(ALUMNO, on_delete=models.CASCADE, null=True)
    CURSO = models.ForeignKey(CURSO, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.year + ' ' + self.ALUMNO + ' ' + self.CURSO

class ASIGNATURA(models.Model):
    nombre_asigantura = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_asigantura

    
class EVALUACION(models.Model):
    fecha_evaluacion = models.DateField()
    ASIGNATURA = models.ForeignKey(ASIGNATURA, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.fecha_evaluacion + ' ' + self.ASIGNATURA

class DETALLE_EVALUACION(models.Model):
    nota = models.FloatField()
    EVALUACION = models.ForeignKey(EVALUACION, on_delete=models.CASCADE, null=True)
    ALUMNO = models.ForeignKey(to = ALUMNO, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nota + ' ' + self.EVALUACION + ' ' + self.ALUMNO

class ACTIVIDAD(models.Model):
    nombre_actividad = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_actividad

class DETALLE_ACTIVIDAD(models.Model):
    fecha_actividad = models.DateField()
    ALUMNO = models.ForeignKey(ALUMNO, on_delete=models.CASCADE, null=True)
    ACTIVIDAD = models.ForeignKey(ACTIVIDAD, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.fecha_actividad + ' ' + self.ALUMNO + ' ' + self.ACTIVIDAD

class DETALLE_JEFATURA(models.Model):
    PROFESOR = models.ForeignKey(PROFESOR, on_delete=models.CASCADE, null=True)
    CURSO = models.ForeignKey(CURSO, on_delete=models.CASCADE, null=True)
