# Generated by Django 2.2.6 on 2019-10-26 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0010_auto_20191026_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pregunta',
            old_name='texto',
            new_name='pregunta',
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='texto',
            new_name='respuesta',
        ),
    ]
