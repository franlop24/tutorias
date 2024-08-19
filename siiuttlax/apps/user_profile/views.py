from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from apps.academy.models import Admin, Professor, Student


def login_view(request):
    form = AuthenticationForm(request, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Verifica si el usuario es un estudiante
                try:
                    student = Student.objects.get(user_ptr=user)
                    return redirect('student_dashboard')
                except Student.DoesNotExist:
                    pass

                # Verifica si el usuario es un profesor
                try:
                    professor = Professor.objects.get(user_ptr=user)
                    return redirect('professor_dashboard')
                except Professor.DoesNotExist:
                    pass

                 # Verifica si el usuario es un profesor
                try:
                    admin = Admin.objects.get(user_ptr=user)
                    return redirect('admin_dashboard')
                except Professor.DoesNotExist:
                    pass

                # Si no es ni estudiante ni profesor, redirige a home
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    
    return render(request, 'login/login.html', {'form': form})

@login_required
def student_dashboard(request):
    # Verificar si el usuario autenticado es un estudiante
    try:
        student_profile = request.user.student
        user_type = 'estudiante'
    except Student.DoesNotExist:
        # Si no es estudiante, redirige a la página de inicio
        return render(request, 'profile/error_404.html', {'message': 'No se encontró el perfil de estudiante asociado'})
    
    return render(request, 'home/student_dashboard.html', {'user': request.user, 'student': student_profile, 'user_type': user_type})

@login_required
def professor_dashboard(request):
    # Verificar si el usuario autenticado es un profesor
    try:
        professor_profile = request.user.professor
        user_type = 'profesor'
    except Professor.DoesNotExist:
        # Si no es profesor, redirige a la página de inicio
        return render(request, 'profile/error_404.html', {'message': 'No se encontró el perfil asociado al modulo'})
    
    return render(request, 'home/professor_dashboard.html', {'user': request.user, 'professor': professor_profile, 'user_type': user_type})

def custom_404_view(request, exception):
    return render(request, 'profile/error_404.html', {'message': 'No se encontró el perfil asociado al modulo'})

@login_required
def admin_dashboard(request):
    # Verificar si el usuario autenticado es un profesor
    try:
        admin_profile = request.user.admin
        user_type = 'administrador'
    except Admin.DoesNotExist:
        # Si no es profesor, redirige a la página de inicio
        return render(request, 'profile/error_404.html', {'message': 'No se encontró el perfil asociado al modulo'})
    
    return render(request, 'home/admin_dbar.html', {'user': request.user, 'admin': admin_profile ,'user_type': user_type})

def custom_404_view(request, exception):
    return render(request, 'profile/error_404.html', {'message': 'No se encontró el perfil asociado al modulo'})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileUpdateForm
from apps.academy.models import Professor, Student

@login_required
def update_profile(request):
    user = request.user  # Obtener el usuario actualmente autenticado
    
    if request.method == 'POST':
        user_form = ProfileUpdateForm(request.POST, instance=user)
        if user_form.is_valid():
            user = user_form.save()

            # Actualizar matrícula si el usuario es un estudiante
            if hasattr(user, 'student'):
                enrollment = user_form.cleaned_data.get('enrollment')
                if enrollment:
                    user.student.enrollment = enrollment
                    user.student.save()

            messages.success(request, '¡Tu perfil ha sido actualizado!')
            update_session_auth_hash(request, user)  # Actualizar la sesión del usuario si cambió la contraseña

            # Redirigir al dashboard correspondiente
            if hasattr(user, 'student'):
                return redirect('student_dashboard')
            elif hasattr(user, 'professor'):
                return redirect('professor_dashboard')
            else:
                return redirect('home')
    else:
        user_form = ProfileUpdateForm(instance=user)
    
    return render(request, 'profile/update_profile.html', {'user_form': user_form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileForm, ProfileUpdateForm
from apps.academy.models import Professor, Student
from apps.academy.models import Profile

@login_required
def update_perfil(request):
    user = request.user
    
    # Verificar si el usuario tiene un perfil, si no, crear uno
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado!')
            
            if hasattr(user, 'student'):
                return redirect('student_dashboard')
            elif hasattr(user, 'professor'):
                return redirect('professor_dashboard')
            else:
                return redirect('home')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'profile/update_perfil.html', {'profile_form': profile_form})

from django.shortcuts import redirect

def home(request):
    user = request.user
    if hasattr(user, 'student'):
        return redirect('student_dashboard')
    elif hasattr(user, 'professor'):
        return redirect('professor_dashboard')
    elif hasattr(user, 'admin'):
        return redirect('admin_dashboard')
    else:
        return redirect('/')  # Redirigir a la página inicial si no tiene un perfil específico


















