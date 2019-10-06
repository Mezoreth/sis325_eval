from django.db import models

# Create your models here.
class Cuestionario(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    materia = models.CharField(max_length=50, null=True, blank=True)

class Tipo(models.Model):
    nombre = models.CharField(max_length=25, null= False, blank= False)

class Pregunta(models.Model):
    texto = models.CharField(max_length=50, null=False, blank= False)
    id_tipo = models.ForeignKey(Tipo, on_delete= models.CASCADE)
    id_cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)

class Respuesta(models.Model):
    texto = models.CharField(max_length=50, null=False, blank= False)
    correcto = models.BooleanField(null=False, blank=False)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)



