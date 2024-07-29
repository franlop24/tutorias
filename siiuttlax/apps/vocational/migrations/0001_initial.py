# Generated by Django 5.0.6 on 2024-07-11 01:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('career', '0004_alter_subject_options'),
        ('library', '0007_alter_question_answer1_alter_question_answer2'),
        ('period', '0002_alter_period_options_alter_semester_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(verbose_name='Etapa')),
                ('application_date', models.DateField(verbose_name='Fecha de aplicacion')),
            ],
            options={
                'verbose_name': 'etapa',
                'verbose_name_plural': 'etapas',
            },
        ),
        migrations.CreateModel(
            name='Breakdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(default='-', max_length=5, verbose_name=' Respuesta')),
                ('correct', models.CharField(default='-', max_length=5, verbose_name='Respuesta correcta')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.question', verbose_name='Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0, verbose_name='Calificacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Carrera')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.period', verbose_name='Periodo')),
                ('questions', models.ManyToManyField(through='vocational.Breakdown', to='library.question', verbose_name='Preguntas')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'examen',
                'verbose_name_plural': 'examenes',
            },
        ),
        migrations.AddField(
            model_name='breakdown',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocational.exam', verbose_name='Examen'),
        ),
        migrations.CreateModel(
            name='ExamModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('score', models.FloatField(default=0.0, verbose_name='Calificación')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocational.exam', verbose_name='Examen')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module', verbose_name='Módulo')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='modules',
            field=models.ManyToManyField(through='vocational.ExamModule', to='library.module', verbose_name='Módulos'),
        ),
    ]