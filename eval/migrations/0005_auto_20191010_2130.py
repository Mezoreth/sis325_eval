# Generated by Django 2.2.6 on 2019-10-11 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0004_auto_20191010_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='tipo',
            field=models.CharField(choices=[('Falso y Verdadero', 'Falso y Verdadero'), ('multiple opcion 1 respuesta', 'Multiple Opcion 1 Respuetsa'), ('multiple opcion multiple respuesta', 'Multiple Opcion Multiple Respuesta')], max_length=45),
        ),
    ]
