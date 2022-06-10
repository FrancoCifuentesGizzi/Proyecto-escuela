from django.contrib.auth.models import AbstractUser
from django.db import models 


class Usuario(AbstractUser):
    email = models.EmailField('email address', unique = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name



class ALUMNO(models.Model):
    rut_alumno=models.CharField(primary_key=True, max_length=15)
    nombre_alumno=models.CharField(max_length=100)
    apellido_alumno=models.CharField(max_length=100)

# class CURSA


# class CURSO


# class ASIGNATURA


# class EVALUACION


# class ACTIVIDAD