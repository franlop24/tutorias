# apps/user_profile/urls.py

from django.urls import path
from .views import admin_dashboard, custom_404_view, login_view, student_dashboard, professor_dashboard, update_perfil, update_profile

urlpatterns = [
    path('login/', login_view, name='Login'),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('professor/dashboard/', professor_dashboard, name='professor_dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('update_profile/', update_profile, name='update_profile'),
    path('update_perfil/', update_perfil, name='update_perfil'),
    path('404/', custom_404_view, name='custom_404_view'),
]
