from atexit import register
from lib2to3.pgen2.token import CIRCUMFLEX
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import DETALLE_JEFATURA, Usuario, ALUMNO, CURSA, CURSO, ASIGNATURA, EVALUACION, DETALLE_EVALUACION, ACTIVIDAD, DETALLE_ACTIVIDAD

class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ['rut', 'first_name', 'last_name']







admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ALUMNO)
admin.site.register(CURSO)
admin.site.register(CURSA)
admin.site.register(ASIGNATURA)
admin.site.register(EVALUACION)
admin.site.register(ACTIVIDAD)
admin.site.register(DETALLE_EVALUACION)
admin.site.register(DETALLE_ACTIVIDAD)
admin.site.register(DETALLE_JEFATURA)