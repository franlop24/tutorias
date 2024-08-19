# academy/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import StudentRegistrationForm
from apps.vocational.models import Exam

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Combina los apellidos paterno y materno en el campo last_name
            user.last_name = f"{form.cleaned_data['last_name_father']} {form.cleaned_data['last_name_mother']}"
            user.save()
            messages.success(request, '¡Tu cuenta ha sido creada! Puedes iniciar sesión ahora.')
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'login/register.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.group.models import Group
from apps.interview.models import InitialInterview

@login_required
def students_list(request):
    professor = request.user.professor
    groups = Group.objects.filter(tutor=professor)

    if not groups.exists():
        messages.error(request, 'No tiene ningún grupo asignado.')
        return render(request, 'interview/students_list.html', {
            'groups': [],
            'selected_group': None,
            'students': []
        })

    selected_group_id = request.GET.get('group_id')
    selected_group = groups.filter(id=selected_group_id).first() if selected_group_id else None

    students = []
    if selected_group:
        interviews = InitialInterview.objects.filter(grupo_escolar=selected_group)
        students = [interview.student for interview in interviews if interview.student]
        

    return render(request, 'interview/students_list.html', {
        'groups': groups,
        'selected_group': selected_group,
        'students': students
    })

@login_required
def reactivate_interview(request, student_id):
    interview = get_object_or_404(InitialInterview, student_id=student_id)
    interview.active = True
    interview.save()
    messages.success(request, 'La entrevista inicial ha sido reactivada.')
    return redirect('students_list')

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.interview.models import InitialInterview

@login_required
def view_interview(request, student_id):
    interview = get_object_or_404(InitialInterview, student__id=student_id)
    return render(request, 'interview/view_interview.html', {
        'interview': interview
    })

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfessorForm
from .models import Professor

@login_required
def create_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.set_password(form.cleaned_data['password'])  # Para guardar la contraseña correctamente
            # Combina los apellidos paterno y materno en el campo last_name
            professor.last_name = f"{form.cleaned_data['last_name_father']} {form.cleaned_data['last_name_mother']}"
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
            # Combina los apellidos paterno y materno en el campo last_name
            admin.last_name = f"{form.cleaned_data['last_name_father']} {form.cleaned_data['last_name_mother']}"
            admin.save()
            return redirect('Login')  # Redirige a la vista deseada después de crear el administrador
    else:
        form = AdminForm()
    
    return render(request, 'login/admin_register.html', {'form': form})










