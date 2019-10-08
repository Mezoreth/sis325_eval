from django.forms import ModelForm
from .models import Cuestionario ,Pregunta, Respuesta

class cuestionario_form(ModelForm):
    class Meta:
        model = Cuestionario
        fields = ['titulo','materia']

class pregunta_form(ModelForm):
    class Meta:
        model = Pregunta
        fields = ['texto', 'puntaje']
        #fields = ('texto', 'titulo',)

class respuesta_form(ModelForm):
    class Meta:
        model = Respuesta
        fields = ['texto','correcto']
        #fields = ('texto', 'correcto', )