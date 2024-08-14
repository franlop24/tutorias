# En user_profile/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    TIPO_SANGRE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True, null=True, verbose_name='Biografía')
    sexo = models.CharField(blank=True, null=True, max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo')
    age = models.IntegerField(blank=True, null=True, verbose_name='Edad')
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')
    lugar_nacimiento = models.CharField(blank=True, null=True, max_length=200, verbose_name='Lugar de nacimiento')
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')
    celular = models.CharField(blank=True, null=True, max_length=15, verbose_name='Teléfono Celular')
    telefono_emergencia = models.CharField(blank=True, null=True, max_length=15, verbose_name='Teléfono de emergencia')
    numero_seguro_social = models.CharField(blank=True, null=True, max_length=20, verbose_name='Número de seguro social')
    tipo_sangre = models.CharField(blank=True, null=True, max_length=3, choices=TIPO_SANGRE_CHOICES, verbose_name='Tipo de sangre')

    def __str__(self):
        return self.user.username

class Address(models.Model):
    pass







