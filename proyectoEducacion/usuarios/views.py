from django.shortcuts import render

from .models import Persona

from .forms import PersonaForm

from django.http import JsonResponse 
from django.template.loader import render_to_string

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'lista_personas.html', {'personas': personas})

def agregar_persona(request):
    data = dict()

    if request.method == "POST":
        form = PersonaForm(request.POST)
        
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = PersonaForm()

    context = {'form': form}
    
    data['html_form'] = render_to_string('formulario_agregar_personas.html', context, request=request)
    
    
    return JsonResponse(data)

