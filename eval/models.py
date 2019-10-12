from django.db import models

# Create your models here.
class Cuestionario(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    materia = models.CharField(max_length=50, null=True, blank=True)
    duracion = models.PositiveSmallIntegerField(default=60)
    repeticiones = models.PositiveSmallIntegerField(default=1)
    ver_r_correctas = models.BooleanField(default=False)
    ver_r_incorectas = models.BooleanField(default=False)
    envio = models.CharField(max_length=15, blank= True)

class Pregunta(models.Model):
    texto = models.CharField(max_length=50, null=False, blank= False)
    tipos =(('Falso y Verdadero','Falso y Verdadero'),('multiple opcion 1 respuesta','Multiple Opcion 1 Respuetsa'),('multiple opcion multiple respuesta','Multiple Opcion Multiple Respuesta'))
    tipo = models.CharField(max_length=15, null=False, blank=False)

class Respuesta(models.Model):
    texto = models.CharField(max_length=50, null=False, blank= False)
    correcto = models.BooleanField(null=False, blank=False)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

class Pregunta_de_Cuestionario(models.Model):
    puntaje = models.PositiveSmallIntegerField(null= False, blank= False)
    id_pregunta = models.ForeignKey(Pregunta, on_delete= models.CASCADE)
    id_cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)

