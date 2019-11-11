from django.db import models
from django.urls import reverse
# Create your models here.
class Cuestionario(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    duracion = models.PositiveSmallIntegerField(default=60)
    repeticiones = models.PositiveSmallIntegerField(default=1)
    ver_r_correctas = models.BooleanField(default=False)
    ver_r_incorectas = models.BooleanField(default=False)
    OPCIONES = (('automatico','Automatico'),('manual','Manual'),('ambos','Ambos'))
    envio = models.CharField(max_length=10, choices=OPCIONES, default='ambos')
    estado = models.BooleanField(default=False)
    clave = models.CharField(max_length=25, blank=True)
    def __str__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('detalle_cuestionario', kwargs={'pk': self.pk})

class Materia(models.Model):
    nombre = models.CharField(max_length=50, unique= True)
    sigla = models.CharField(max_length=7, unique= True)
    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=50, null=False, blank=False)
    tipos = (('A','Falso y Verdadero'),('B','Multiple Opcion 1 Respuetsa'),('C','Multiple Opcion Multiple Respuesta'))
    tipo = models.CharField(max_length=45, choices=tipos, null=False, blank=False)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    def __str__(self):
        return self.pregunta
    def get_absolute_url(self):
        return reverse('detalle_pregunta', kwargs={'pk': self.pk})

class Respuesta(models.Model):
    respuesta = models.CharField(max_length=50, null=False, blank= False)
    correcto = models.BooleanField(default=False)
    valor = models.FloatField(null=True, blank=True)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.respuesta

class PreguntaCuestionario(models.Model):
    puntaje = models.PositiveSmallIntegerField(null=False, blank=False, default=10)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    id_cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE,)
