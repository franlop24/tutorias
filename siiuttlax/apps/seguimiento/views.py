from django.shortcuts import render
from apps.academy.models import Student, Professor
from .models import Career  # Asegúrate de importar el modelo Career


def index(request):
    careers = Career.objects.all()  # Obtén todas las carreras
    students = Student.objects.all()  # Obtén todos los estudiantes
    professors= Professor.objects.all()  # Obtén todos los estudiantes
    return render(request, 'seguimiento/index.html', {'careers': careers, 'students': students, 'professors':professors})

