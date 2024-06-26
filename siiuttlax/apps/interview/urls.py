# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('fill-initial-interview/', views.fill_initial_interview, name='fill_initial_interview'),
    # Otras URLs de tu aplicación
]
