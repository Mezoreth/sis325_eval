from django.contrib import admin
from .models import Cuestionario, Pregunta, Respuesta, Pregunta_de_Cuestionario
# Register your models here.

admin.site.register(Cuestionario)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Pregunta_de_Cuestionario)