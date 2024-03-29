# Generated by Django 2.2.6 on 2019-11-18 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0024_docente_estudiante_estudiantecuestionario_respuestaelegida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestaelegida',
            name='id_ecuestionario',
        ),
        migrations.AlterField(
            model_name='docente',
            name='ci',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='PreguntaObtenida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.FloatField(default=0)),
                ('id_ecuestionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.EstudianteCuestionario')),
                ('id_preguntac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.PreguntaCuestionario')),
            ],
        ),
        migrations.AddField(
            model_name='respuestaelegida',
            name='id_preguntao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eval.PreguntaObtenida'),
            preserve_default=False,
        ),
    ]
