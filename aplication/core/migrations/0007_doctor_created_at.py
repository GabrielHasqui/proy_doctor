# Generated by Django 5.1.2 on 2024-11-03 04:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_paciente_cedula'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Creación'),
        ),
    ]
