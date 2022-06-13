from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    # variable de session num_visitas.
    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas + 1
    
    # default template.
    template = loader.get_template('home.html')
    context = {
        'settings': settings,
        'dataarticulos': None,
        'num_visitas': num_visitas,
    }

    if (request.user.is_authenticated):    
        # es superusuario?
        if (request.user.is_superuser):
            return HttpResponseRedirect('admin/')
        if (len(request.user.groups.all()) > 0):
            # revisar el grupo (el primero).
            grupo = request.user.groups.all()[0]
            
            # cambia el template.
            if (grupo.name == "Profesor"):
                template = loader.get_template('cursos/dashboard.html')
            if (grupo.name == "Apoderado"):
                template = loader.get_template('cursos/dashboard.html')
            
            else:
                # otros grupos.
                pass
        else:
            # usuario sin grupo.
            pass
    else:
        # usuario no autenticado.
        pass
    return HttpResponse(template.render(context, request))