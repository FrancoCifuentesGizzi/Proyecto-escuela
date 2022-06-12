from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def home(request):
    # variable de session num_visitas.
    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas + 1
    
    # default template.
    template = loader.get_template('index.html')
    context = {
        'settings': settings,
        'dataarticulos': None,
        'num_visitas': num_visitas,
    }
    return HttpResponse(template.render(context, request))