from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



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
    return HttpResponse(template.render(context, request))
