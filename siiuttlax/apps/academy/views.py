# academy/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import StudentRegistrationForm

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '¡Tu cuenta ha sido creada! Puedes iniciar sesión ahora.')
            return redirect('Login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'login/register.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.group.models import Group
from apps.interview.models import InitialInterview 

@login_required
def students_list(request):
    # Obtener al tutor (Professor) asociado al usuario actual
    professor = request.user.professor

    # Obtener el grupo del tutor (Professor)
    group = Group.objects.filter(tutor=professor).first()

    # Validar si se encontró el grupo del tutor
    if group:
        # Obtener las entrevistas iniciales asociadas al grupo escolar del tutor
        interviews = InitialInterview.objects.filter(grupo_escolar=group)

        # Obtener los estudiantes asociados a través de las entrevistas
        students = [interview.student for interview in interviews if interview.student]  # Filtra estudiantes no nulos

        return render(request, 'interview/students_list.html', {
            'group': group,
            'students': students
        })
    else:
        # Manejar el caso donde el tutor no tiene asignado ningún grupo
        return render(request, 'interview/students_list.html', {
            'group': None,
            'students': []
        })
    
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Professor
from .forms import ProfessorForm

@login_required
def create_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.set_password(form.cleaned_data['password'])  # Para guardar la contraseña correctamente
            professor.save()
            return redirect('admin_dashboard')  # Redirige a la vista deseada después de crear el profesor
    else:
        form = ProfessorForm()
    
    professors = Professor.objects.all()  # Obtener la lista de profesores
    return render(request, 'manage/admin_create_professor.html', {'form': form, 'professors': professors})

from django.shortcuts import render, redirect
from .forms import AdminForm

def register_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.set_password(form.cleaned_data['password1'])  # Para guardar la contraseña correctamente
            admin.save()
            return redirect('Login')  # Redirige a la vista deseada después de crear el administrador
    else:
        form = AdminForm()
    
    return render(request, 'login/admin_register.html', {'form': form})









