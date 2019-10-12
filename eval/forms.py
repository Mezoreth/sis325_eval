from django import forms
from django.forms import ModelForm
from .models import Cuestionario ,Pregunta, Respuesta

class cuestionario_form(ModelForm):
    class Meta:
        model = Cuestionario
        fields = '__all__'
        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'materia':forms.TextInput(attrs={'class':'form-control'}),
        }
class pregunta_form(ModelForm):
    class Meta:
        model = Pregunta
        fields = '__all__'
        #fields = ('texto', 'titulo',)
        widgets = {
            'texto':forms.Textarea(attrs={'class':'form-control'}),
        }
class respuesta_form(ModelForm):
    class Meta:
        model = Respuesta
        fields = ['texto','correcto']
        #fields = ('texto', 'correcto', )
        widgets = {
            'texto':forms.TextInput(attrs={'class':'form-control'}),
            'correcto':forms.TextInput(attrs={'class':'form-control'}),
            'id_pregunta':forms.TextInput(attrs={'class':'form-control'}),
        }