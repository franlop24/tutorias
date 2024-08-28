# models.py
from django.db import models

class Career(models.Model):
    level = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    status = models.IntegerField()
    year_plan = models.IntegerField()

class UserProfile(models.Model):
    sexo = models.CharField(max_length=1)  # Por ejemplo, 'M' para masculino, 'F' para femenino

class Student(models.Model):
    enrollment = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
