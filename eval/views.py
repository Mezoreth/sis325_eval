from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import *
from .models import Cuestionario, Pregunta, Respuesta, PreguntaCuestionario, Materia, EstudianteCuestionario, PreguntaObtenida, RespuestaElegida, Estudiante, Docente
from django.views.generic.edit import CreateView, UpdateView ,DeleteView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def index_d(request):
    return render_to_response('index_d.html')

def index_e(request):
    return render_to_response('index_e.html')

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
def comprobar_clave(request):
    url = str(reverse_lazy('cuestionarios_disponibles'))
    if request.method == 'GET':
        clave = request.GET.get('clave')
        pk = int(request.GET.get('id'))
        print(clave)
        cuestionario = Cuestionario.objects.get(pk=pk)
        if str(cuestionario.clave) == str(clave):
            url = str(reverse_lazy('examen'))
            return redirect(url)
    return redirect(url)
# metodo de calcular la calificacion
def calcular_calificacion(id):
    ecuest = EstudianteCuestionario.objects.get(pk=id)
    pregunta_obt = PreguntaObtenida.objects.filter(id_ecuestionario__pk=id)
    puntaje_total = 0
    for preg in pregunta_obt:
        respuesta_e = RespuestaElegida.objects.filter(id_preguntao__pk=preg.pk)
        tipo = preg.id_preguntac.id_pregunta.tipo
        puntaje_porc = 0
        puntaje_cuest += preg.id_preguntac.puntaje
        for resp in respuesta_e:
            resp_correcta = resp.id_respuesta.correcto
            # preguntas falso verdadero 
            if tipo == 'A':
                if resp.eleccion == resp_correcta:
                    puntaje_porc = 100
            # pregunta multiple una sola respuesta
            elif tipo == 'B':
                if resp_correcta and resp.eleccion:
                    puntaje_porc = 100
            # pregunta multiples respuestas
            elif  tipo == 'C':
                if resp_correcta == resp.eleccion:
                    puntaje_porc += resp.id_respuesta.valor
        if puntaje_porc > 0:
            puntaje_cuestionario = preg.id_preguntac.puntaje
            puntaje_total = (puntaje_cuestionario*puntaje_porc)/100
            preg.puntaje = puntaje_total
            preg.save(update_fields=['puntaje'])
    calificacion = PreguntaObtenida.objects.filter(id_ecuestionario__pk=id).aggregate(Sum('puntaje'))
    calificacion_total = (calificacion/puntaje_cuest) * 100
    ecuest.calificacion = calificacion_total
    ecuest.save(update_fields=['calificacion'])


# -------------------------------------Estudiante------------------------------------------------
class Estudiante_Elegir(TemplateView):
    template_name = "estudiante_cuestionario_elegir.html"

class Estudiante_ListarCuestionarios_disponibles(ListView): 
    model = Cuestionario
    template_name = 'estudiante_listar_cuestionarios.html'
    queryset = Cuestionario.objects.filter(habilitar=True)

class Estudiante_ListarMaterias(ListView): 
    model = Materia
    template_name = 'estudiante_listar_materias.html'

class Estudiante_ExamenHecho(LoginRequiredMixin, ListView): 
    model = EstudianteCuestionario
    template_name = 'estudiante_listar_cuestionarios_realizados.html'
    def get_queryset(self):
        estudiante = self.request.user
        object_list = EstudianteCuestionario.objects.filter(id_usuario__id=estudiante.id)
        return object_list

class Estudiante_Examen(DetailView): 
    model = Cuestionario
    template_name = 'estudiante_cuestionario_examen.html'