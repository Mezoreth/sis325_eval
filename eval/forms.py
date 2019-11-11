from django import forms
from django.forms import ModelForm
from .models import Cuestionario ,Pregunta, Respuesta, PreguntaCuestionario, Materia
from extra_views import ModelFormSetView

class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

class CuestionarioForm(ModelForm):
    class Meta:
        model = Cuestionario
        fields = ['titulo','duracion','repeticiones','ver_r_correctas','ver_r_incorectas','envio']
        
class PreguntaFVForm(ModelForm):
    class Meta:
        model = Pregunta
        fields = ['pregunta','id_materia']
        labels = {'pregunta': 'Pregunta descripcion'}
        
class PreguntaMRUForm(ModelForm):
    tps = (('B','Multiple Opcion 1 Respuetsa'),('C','Multiple Opcion Multiple Respuesta'))
    tipo = forms.ChoiceField(choices=tps,initial='B',disabled=True)
    class Meta:
        model = Pregunta
        fields = ['pregunta','tipo','id_materia']

class PreguntaMRMForm(ModelForm):
    tps = (('B','Multiple Opcion 1 Respuetsa'),('C','Multiple Opcion Multiple Respuesta'))
    tipo = forms.ChoiceField(choices=tps,initial='C',disabled=True)
    class Meta:
        model = Pregunta
        fields = ['pregunta','tipo','id_materia']

class RespuestaVForm(ModelForm):
    correcto = forms.BooleanField(initial=True, disabled=True)
    class Meta:
        model = Respuesta
        fields = ['respuesta','correcto']

class RespuestaForm(ModelForm):
    class Meta:
        model = Respuesta
        fields = ['respuesta','correcto']
        labels = {'respuesta': 'Respuesta descripcion'}

class PreguntaForm(ModelForm):
    tipo = forms.CharField(disabled=True)
    class Meta:
        model = Pregunta
        fields = ['pregunta','tipo','id_materia']

class PreguntaCuestionarioForm(ModelForm):
    class Meta:
        model = PreguntaCuestionario
        fields = '__all__'