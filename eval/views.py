from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.shortcuts import render_to_response
from .forms import cuestionario_form, pregunta_form, respuesta_form
from .models import Cuestionario, Pregunta, Respuesta
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
    return render_to_response('index.html')

#####################################################    Cuestionarios
class crear_cuestionarios(CreateView):
    form_class = cuestionario_form
    template_name = 'cuestionario_nuevo.html'
    
class listar_cuestionarios(ListView):
    model = Cuestionario
    template_name = 'cuestionario_listar.html'
class editar_cuestionarios(UpdateView):
    model = Cuestionario
    form_class = cuestionario_form
    template_name='cuestionario_editar.html'
    success_url = reverse_lazy('cuestionario_l')

class ver_cuestionarios(DetailView):
    model = Cuestionario
    template_name='cuestionario_ver.html'

class eliminar_cuestionarios(DeleteView):
    model = Cuestionario
    form_class = cuestionario_form
    success_url = reverse_lazy('cuestionario_l')

class crear_pregunta(CreateView):
    form_class = pregunta_form
    template_name = 'pregunta_crear.html'

class crear_respuesta(CreateView):
    form_class = respuesta_form
    template_name = 'respuesta_crear.html'



    