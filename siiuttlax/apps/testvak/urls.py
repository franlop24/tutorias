#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('fill_testv_interview/', views.fill_testv_interview, name='fill_testv_interview'),
    path('fill_testhe_interview/', views.fill_testhe_interview, name='fill_testhe_interview'),
]