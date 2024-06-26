# urls.py
from django.urls import path
from .views import create_professor, register, register_admin, students_list

urlpatterns = [
    path('register/', register, name='register'),
    path('students/', students_list, name='students_list'),
    path('create_p/', create_professor, name='create_professor'),
    path('register_admin/', register_admin, name='register_admin'),
    # otras rutas
]
