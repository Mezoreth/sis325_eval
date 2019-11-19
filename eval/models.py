from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Cuestionario(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    duracion = models.PositiveSmallIntegerField(default=60)
    repeticiones = models.PositiveSmallIntegerField(default=1)
    ver_r_correctas = models.BooleanField(default=False)
    ver_r_incorectas = models.BooleanField(default=False)
    OPCIONES = (('automatico','Automatico'),('manual','Manual'),('ambos','Ambos'))
    envio = models.CharField(max_length=10, choices=OPCIONES, default='ambos')
    habilitar = models.BooleanField(default=False)
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
    id_cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_pregunta

class Docente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ci = models.IntegerField(default=0)
    privilegio = models.IntegerField(default=1)
    def __str__(self):
        return self.user.username

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cu = models.CharField(max_length=10, blank=True)
    privilegio = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

class EstudianteCuestionario(models.Model):
    calificacion = models.FloatField(default=0)
    intentos = models.IntegerField()
    id_usuario = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_cuestionario = models.ForeignKey(Cuestionario, on_delete=models.PROTECT)
    def __str__(self):
        return self.id_cuestionario.titulo

class PreguntaObtenida(models.Model):
    puntaje = models.FloatField(default=0)
    id_ecuestionario = models.ForeignKey(EstudianteCuestionario, on_delete=models.CASCADE)
    id_preguntac = models.ForeignKey(PreguntaCuestionario, on_delete=models.CASCADE)

class RespuestaElegida(models.Model):
    eleccion = models.BooleanField(default=False)
    id_preguntao = models.ForeignKey(PreguntaObtenida, on_delete=models.CASCADE)
    id_respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)