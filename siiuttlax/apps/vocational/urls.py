from django.urls import path
from . import views

app_name = 'vocational'
urlpatterns = [
    path('', views.home, name='home'),
    path('test/<int:q_id>/', views.test, name='test'),
    path('results/', views.results, name='results'),
]
