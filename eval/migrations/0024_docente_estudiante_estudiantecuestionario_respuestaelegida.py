# Generated by Django 2.2.6 on 2019-11-18 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eval', '0023_auto_20191117_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cu', models.CharField(blank=True, max_length=10)),
                ('privilegio', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteCuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.FloatField(default=0)),
                ('intentos', models.IntegerField()),
                ('id_cuestionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eval.Cuestionario')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaElegida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eleccion', models.BooleanField(default=False)),
                ('id_ecuestionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.EstudianteCuestionario')),
                ('id_respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.Respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.IntegerField(blank=True)),
                ('privilegio', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
