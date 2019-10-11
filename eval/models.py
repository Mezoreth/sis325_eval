from django.db import models

# Create your models here.
class Cuestionario(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    materia = models.CharField(max_length=50, null=True, blank=True)

class Pregunta(models.Model):
    texto = models.CharField(max_length=50, null=False, blank= False)
    puntaje = models.PositiveSmallIntegerField(null=False, blank=False)
    tipos =(('Falso y Verdadero','Falso y Verdadero'),('multiple opcion 1 respuesta','Multiple Opcion 1 Respuetsa'),('multiple opcion multiple respuesta','Multiple Opcion Multiple Respuesta'))
    tipo = models.CharField(max_length=45, choices=tipos,null=False, blank= False)
    id_cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)

class Respuesta(models.Model):
    texto = models.CharField(max_length=50, null=False, blank= False)
    correcto = models.BooleanField(null=False, blank=False)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)



