# Generated by Django 2.2.6 on 2019-10-26 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0009_auto_20191026_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='id_pregunta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eval.Pregunta'),
        ),
    ]
