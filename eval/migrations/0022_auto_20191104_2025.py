# Generated by Django 2.2.6 on 2019-11-05 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0021_auto_20191029_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuestionario',
            name='clave',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
