# Generated by Django 2.2.6 on 2019-10-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0002_pregunta_puntaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='id_tipo',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tipo',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
    ]
