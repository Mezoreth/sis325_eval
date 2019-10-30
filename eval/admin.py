from django.contrib import admin
from .models import Cuestionario, Pregunta, Respuesta, PreguntaCuestionario, Materia
# Register your models here.

admin.site.register(Cuestionario)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(PreguntaCuestionario)
admin.site.register(Materia)