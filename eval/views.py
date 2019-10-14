from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.shortcuts import render_to_response
from .forms import cuestionario_form, pregunta_form, respuesta_form, pregunta_cuestionario_form
from .models import Cuestionario, Pregunta, Respuesta,  Pregunta_de_Cuestionario
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
    model = Pregunta_de_Cuestionario
    template_name='cuestionario_ver.html'
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context= super(ver_cuestionarios, self).get_context_data(**kwargs)
        context['cuestionario']=Pregunta_de_Cuestionario.objects.filter(id_cuestionario=pk).first()
        context['preguntas']= Pregunta_de_Cuestionario.objects.select_related('id_cuestionario').filter(id_cuestionario=pk)
        context['respuestas']= Respuesta.objects.all()
        return context
    
class eliminar_cuestionarios(DeleteView):
    model = Cuestionario
    form_class = cuestionario_form
    success_url = reverse_lazy('cuestionario_l')

#####################################################    Pregunta

class crear_preguntas(CreateView):
    form_class = pregunta_form
    second_form_class =  Respuesta
    template_name = 'pregunta_crear.html'
    success_url = reverse_lazy('pregunta_l')

class listar_preguntas(ListView): 
    model = Pregunta
    template_name = 'pregunta_listar.html'

class editar_preguntas(UpdateView):
    model = Pregunta
    form_class = pregunta_form
    template_name='pregunta_editar.html'
    success_url = reverse_lazy('pregunta_l')

class eliminar_preguntas(DeleteView):
    model = Pregunta
    success_url= reverse_lazy('pregunta_l')

#####################################################    Respuesta

class crear_respuestas(CreateView):
    model = Respuesta
    fields = ['texto', 'correcto']
    template_name = 'respuesta_crear.html'
    success_url = reverse_lazy('pregunta_l')
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        self.fk = pk
        context= super(crear_respuestas,self).get_context_data(**kwargs)
        context['pregunta']=Pregunta.objects.filter(pk=pk).first()
        context['respuesta']=Respuesta.objects.filter(pk=pk).first()
        return context
    def form_valid(self, form, **kwargs):
        fk=self.kwargs.get('pk')
        form.instance.id_pregunta = Pregunta.objects.filter(pk=fk).first()
        return super(crear_respuestas, self).form_valid(form)

class editar_respuestas(UpdateView):
    model = Respuesta
    fields = ['texto','correcto']
    template_name = 'respuesta_editar.html'

class eliminar_respuestas(DeleteView):
    model = Respuesta
    success_url = reverse_lazy('respuesta_l')



    