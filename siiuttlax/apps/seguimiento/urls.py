from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('prueba/',views.Career,name="career"),

    path('seguimiento/', views.index, name='seguimiento'),
]