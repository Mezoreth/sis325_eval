# Generated by Django 2.2.6 on 2019-10-27 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0011_auto_20191026_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Falso y Verdadero', 'Falso y Verdadero'), ('multiple opcion 1 respuesta', 'Multiple Opcion 1 Respuetsa'), ('multiple opcion multiple respuesta', 'Multiple Opcion Multiple Respuesta')], max_length=45, null=True),
        ),
    ]
