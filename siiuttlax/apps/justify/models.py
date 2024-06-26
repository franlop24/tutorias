from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Justificante(models.Model):
    alumno = models.CharField(max_length=255)
    grupo = models.CharField(max_length=10)
    carrera = models.CharField(max_length=255)
    tsu = models.BooleanField(default=False)
    ingenieria = models.BooleanField(default=False)
    dias_falta = models.CharField(max_length=255)
    motivo = models.CharField(max_length=255)
    profesores = models.ManyToManyField(User, related_name='profesores_justificantes')
    adjuntar_archivos = models.FileField(upload_to='justificantes/', blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    mes = models.CharField(max_length=20)
    anio = models.CharField(max_length=4, default='2024')

    def __str__(self):
        return f"Justificante de {self.alumno} para {self.dias_falta}"