from django import forms
from django.forms import ModelForm
from .models import Cuestionario ,Pregunta, Respuesta, PreguntaCuestionario, Materia
from extra_views import ModelFormSetView

class MateriaForm(ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    class Meta:
        model = Materia
        fields = '__all__'

class CuestionarioForm(ModelForm):
    class Meta:
        model = Cuestionario
        fields = ['titulo','duracion','repeticiones','ver_r_correctas','ver_r_incorectas','envio']
        
class PreguntaFVForm(ModelForm):
    pregunta = forms.CharField(widget=forms.TextInput(attrs={'size': '75'}))
    class Meta:
        model = Pregunta
        fields = ['pregunta','id_materia']
        labels = {'pregunta': 'Pregunta descripcion'}
        
class PreguntaMRUForm(ModelForm):
    pregunta = forms.CharField(widget=forms.TextInput(attrs={'size': '75'}))
    tps = (('B','Multiple Opcion 1 Respuetsa'),('C','Multiple Opcion Multiple Respuesta'))
    tipo = forms.ChoiceField(choices=tps,initial='B',disabled=True)
    class Meta:
        model = Pregunta
        fields = ['pregunta','tipo','id_materia']

class PreguntaMRMForm(ModelForm):
    pregunta = forms.CharField(widget=forms.TextInput(attrs={'size': '75'}))
    tps = (('B','Multiple Opcion 1 Respuetsa'),('C','Multiple Opcion Multiple Respuesta'))
    tipo = forms.ChoiceField(choices=tps,initial='C',disabled=True)
    class Meta:
        model = Pregunta
        fields = ['pregunta','tipo','id_materia']

class RespuestaVForm(ModelForm):
    respuesta = forms.CharField(widget=forms.TextInput(attrs={'size': '75'}))
    correcto = forms.BooleanField(initial=True, disabled=True)
    class Meta:
        model = Respuesta
        fields = ['respuesta','correcto']

class RespuestaForm(ModelForm):
    respuesta = forms.CharField(widget=forms.TextInput(attrs={'size': '75'}))
    valor = forms.CharField(widget=forms.TextInput(attrs={'size': '5'}))
    class Meta:
        model = Respuesta
        fields = ['respuesta','correcto']
        labels = {'respuesta': 'Respuesta descripcion'}

class PreguntaForm(ModelForm):
    pregunta = forms.CharField(widget=forms.TextInput(attrs={'size': '75'}))
    tipo = forms.CharField(disabled=True)
    class Meta:
        model = Pregunta
        fields = ['pregunta','tipo','id_materia']

class PreguntaCuestionarioForm(ModelForm):
    class Meta:
        model = PreguntaCuestionario
        fields = '__all__'