# En academy/models.py
from django.db import models
from apps.user_profile.models import  Profile
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.short_name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'

class Professor(User):
    title = models.CharField(max_length=50, verbose_name='Título')
    employee_number = models.IntegerField(verbose_name='Número de Empleado')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría', null=True, blank=True)

    @property
    def full_name(self):
        return f"{ self.first_name } { self.last_name }"
    
    def __str__(self):
        return f"{ self.title } - { self.full_name }"

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'


class Student(User):
    enrollment = models.CharField(blank=True, null=True,max_length=12, verbose_name='Matrícula')
    
    @property
    def full_name(self):
        return f"{ self.first_name } { self.last_name }"
     
    def __str__(self):
        return f"{ self.full_name } - { self.enrollment }"
    
    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'


class Admin(User):
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.username} - {self.full_name}"

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
