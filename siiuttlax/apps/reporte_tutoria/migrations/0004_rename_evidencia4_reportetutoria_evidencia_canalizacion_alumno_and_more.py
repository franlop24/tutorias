# Generated by Django 5.0.6 on 2024-07-22 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporte_tutoria', '0003_reportetutoria_evidencia4_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportetutoria',
            old_name='evidencia4',
            new_name='evidencia_canalizacion_alumno',
        ),
        migrations.RenameField(
            model_name='reportetutoria',
            old_name='evidencia3',
            new_name='evidencia_evidencia_audio',
        ),
        migrations.RenameField(
            model_name='reportetutoria',
            old_name='evidencia1',
            new_name='evidencia_fotografica',
        ),
        migrations.RenameField(
            model_name='reportetutoria',
            old_name='evidencia2',
            new_name='evidencia_lista_asistencia',
        ),
    ]
