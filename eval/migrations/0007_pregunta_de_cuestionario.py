# Generated by Django 2.2.6 on 2019-10-12 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0006_auto_20191012_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta_de_Cuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.PositiveSmallIntegerField()),
                ('id_cuestionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.Cuestionario')),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eval.Pregunta')),
            ],
        ),
    ]
