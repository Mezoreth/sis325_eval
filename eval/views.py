from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import *
from .models import Cuestionario, Pregunta, Respuesta,  PreguntaCuestionario, Materia
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
# Create your views here.

def index(request):
    return render_to_response('index.html')

def pregunta_tipo(request):
    return render_to_response('pregunta_elegir.html')

#####################################################    Materias
class ListarMaterias(ListView):
    model = Materia
    template_name = 'materia_listar.html'

class CrearMateria(CreateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'materia_crear.html'
    success_url = reverse_lazy('listar_materias')

class EditarMateria(UpdateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'materia_editar.html'
    success_url = reverse_lazy('listar_materias')

class EliminarMateria(DeleteView):
    model = Materia
    template_name='materia_eliminar.html'
    success_url = reverse_lazy('listar_materias')

#####################################################    Cuestionarios
class CrearCuestionario(CreateView):
    form_class = CuestionarioForm
    template_name = 'cuestionario_crear.html'
    success_url = reverse_lazy('listar_cuestionarios')
    
class ListarCuestionarios(ListView): 
    model = Cuestionario
    template_name = 'cuestionario_listar.html'

class EditarCuestionario(UpdateView):
    model = Cuestionario
    form_class = CuestionarioForm
    template_name='cuestionario_editar.html'
    success_url = reverse_lazy('listar_cuestionarios')

class HabilitarCuestionario(UpdateView):
    model = Cuestionario
    fields = ['estado','clave']
    template_name = ''
    success_url = reverse_lazy('')

class DetalleCuestionario(DetailView):
    model = Cuestionario
    template_name='cuestionario_ver.html'
    
class EliminarCuestionario(DeleteView):
    model = Cuestionario
    template_name='cuestionario_eliminar.html'
    success_url = reverse_lazy('listar_cuestionarios')

class AñadirPreguntaCuestionario(ListView):
    model = Pregunta
    template_name = 'pregunta_añadir.html'
    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk')
        return Pregunta.objects.exclude(preguntacuestionario__in=PreguntaCuestionario.objects.filter(id_cuestionario=pk))
    def get_context_data(self,**kwargs):
        context= super(AñadirPreguntaCuestionario,self).get_context_data(**kwargs)
        context['cuestionario_id'] = self.kwargs.get('pk')
        return context

def crear_pregunta_cuestionario(*args, **kwargs):
    try:
        pk_c = kwargs['cuestpk']
        pk_p = kwargs['pregpk']
        cuestionario = Cuestionario.objects.get(pk=pk_c)
        pregunta = Pregunta.objects.get(pk=pk_p)
        pregunta_cuestionario = PreguntaCuestionario(id_cuestionario=cuestionario, id_pregunta= pregunta)
        pregunta_cuestionario.save()
    except:
        pass
    return redirect(cuestionario.get_absolute_url())
####################################################  Preguntas


#   Pregunta multiple opcion una respuesta
class CrearPregunta(TemplateView):
    template_name = "pregunta_elegir.html"

class CrearPreguntaFV(CreateView):
    model = Respuesta
    template_name = 'pregunta_crear_fv.html'
    form_class = RespuestaForm
    second_form_class = PreguntaFVForm
    success_url = reverse_lazy('listar_preguntas')

    def get_context_data(self, **kwargs):
        context = super(CrearPreguntaFV, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context   
    def post(self, request, *args,**kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form2.instance.tipo = 'A'
        if form.is_valid() and form2.is_valid():
            respuesta = form.save(commit=False)
            respuesta.id_pregunta = form2.save()
            respuesta = form.save()
            return HttpResponseRedirect(self.get_success_url())
        else :
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class RespuestaMRUV(InlineFormSetFactory):
    model = Respuesta
    form_class = RespuestaVForm
    fields = ['respuesta','correcto']
    prefix = 'respv'
    factory_kwargs = {'extra': 1, 'max_num': 1,
                      'can_order': False, 'can_delete': False}

class RespuestaMRUF(InlineFormSetFactory):
    model = Respuesta
    fields = ['respuesta']
    prefix = 'respf'
    factory_kwargs = {'extra': 6, 'max_num': 6,
                      'can_order': False, 'can_delete': False}

class CrearPreguntaMRU(CreateWithInlinesView):
    model = Pregunta
    form_class = PreguntaMRUForm
    inlines = [RespuestaMRUV, RespuestaMRUF]
    template_name = 'pregunta_crear_mru.html'
    def get_success_url(self):
        return self.object.get_absolute_url()


#   Pregunta multiple opcion multiple respuesta

class RespuestaMRM(InlineFormSetFactory):
    model = Respuesta
    fields = ['respuesta','correcto','valor']
    factory_kwargs = {'extra': 5, 'max_num': 7,
                      'can_order': False, 'can_delete': False}

class CrearPreguntaMRM(CreateWithInlinesView):
    model = Pregunta
    form_class = PreguntaMRMForm
    inlines = [RespuestaMRM]
    template_name = 'pregunta_crear_mrm.html'
    def get_success_url(self):
        return self.object.get_absolute_url()

####################################################################
class RespuestaEdit(InlineFormSetFactory):
    model = Respuesta
    fields = ['respuesta','correcto','valor']
    factory_kwargs = {'extra': 0, 'max_num': 1,
                      'can_order': False, 'can_delete': False}

class EditarPregunta(UpdateWithInlinesView):
    model = Pregunta
    inlines = [RespuestaEdit]
    form_class = PreguntaForm
    template_name='pregunta_editar.html'
    def get_success_url(self):
        return self.object.get_absolute_url()

class ListarPreguntas(ListView): 
    model = Pregunta
    template_name = 'pregunta_listar.html'

class DetallePregunta(DetailView):
    model = Pregunta
    template_name = 'pregunta_ver.html'

class EliminarPregunta(DeleteView):
    model = Pregunta
    template_name='pregunta_eliminar.html'
    success_url= reverse_lazy('listar_preguntas')
    
################################################################################    Respuesta

class CrearRespuesta(CreateView):
    model = Respuesta
    fields = ['texto', 'correcto']
    template_name = 'respuesta_crear_mr.html'
    success_url = reverse_lazy('listar_preguntas')
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        self.fk = pk
        context= super(CrearRespuesta,self).get_context_data(**kwargs)
        context['pregunta']=Pregunta.objects.filter(pk=pk).first()
        context['respuesta']=Respuesta.objects.filter(pk=pk).first()
        return context
    def form_valid(self, form, **kwargs):
        fk=self.kwargs.get('pk')
        form.instance.id_pregunta = Pregunta.objects.filter(pk=fk).first()
        return super(CrearRespuesta, self).form_valid(form)

class EditarRespuesta(UpdateView):
    model = Respuesta
    fields = ['texto','correcto']
    template_name = 'respuesta_editar.html'

class EliminarRespuesta(DeleteView):
    model = Respuesta
    success_url = reverse_lazy('listar_respuesta')


# metodo de acceso cuestionario
def comprobar_password(request, *args, **kwargs):
    if request.method == 'POST':
        clave = kwargs['clave']
        pk = kwargs['pk']
        cuestionario = Cuestionario.objects.get(pk=pk)
        if str(cuestionario.clave) == str(clave):
            return redirect('')
    return render(request, '')

    