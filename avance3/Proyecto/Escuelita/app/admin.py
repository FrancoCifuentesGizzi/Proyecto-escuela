from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import Usuario, Alumno, Profesor, Curso, Jefatura

class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ['rut', 'first_name', 'last_name']

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido']

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido']

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad_alumnos']

class JefaturaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'profe_jefe']




admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Curso, CursoAdmin)