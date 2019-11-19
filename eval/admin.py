from django.contrib import admin
from .models import Cuestionario, Pregunta, Respuesta, PreguntaCuestionario, Materia, EstudianteCuestionario, RespuestaElegida, Estudiante, Docente
# Register your models here.

admin.site.register(Cuestionario)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(PreguntaCuestionario)
admin.site.register(Materia)
admin.site.register(EstudianteCuestionario)
admin.site.register(RespuestaElegida)
admin.site.register(Estudiante)
admin.site.register(Docente)