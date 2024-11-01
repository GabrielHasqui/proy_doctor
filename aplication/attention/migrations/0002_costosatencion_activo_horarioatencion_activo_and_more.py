# Generated by Django 4.2.16 on 2024-10-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attention', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='costosatencion',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AddField(
            model_name='horarioatencion',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AddField(
            model_name='serviciosadicionales',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='horarioatencion',
            name='dia_semana',
            field=models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miércoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sábado', 'Sábado'), ('domingo', 'Domingo')], max_length=10, unique=True, verbose_name='Día de la Semana'),
        ),
    ]