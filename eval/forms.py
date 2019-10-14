from django import forms
from django.forms import ModelForm
from .models import Cuestionario ,Pregunta, Respuesta, Pregunta_de_Cuestionario

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
        widgets = {
            'texto':forms.Textarea(attrs={'class':'form-control'}),
        }
class respuesta_form(ModelForm):
    class Meta:
        model = Respuesta
        fields = ['texto','correcto']
        widgets = {
            'texto':forms.TextInput(attrs={'class':'form-control'}),
            'correcto':forms.CheckboxInput(attrs={'class':'form-control'}),
        }

class pregunta_cuestionario_form(ModelForm):
    class Meta:
        model = Pregunta_de_Cuestionario
        fields = '__all__'