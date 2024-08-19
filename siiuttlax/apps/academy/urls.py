from django.urls import path
from .views import create_professor, reactivate_interview, register, register_admin, students_list, view_interview

urlpatterns = [
    path('register/', register, name='register'),
    path('students/', students_list, name='students_list'),
    path('reactivate_interview/<int:student_id>/', reactivate_interview, name='reactivate_interview'),
    path('create_p/', create_professor, name='create_professor'),
    path('register_admin/', register_admin, name='register_admin'),
    path('view_interview/<int:student_id>/', view_interview, name='view_interview'),  # Nueva ruta para ver la entrevista
    # otras rutas
]
