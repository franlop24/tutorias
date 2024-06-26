# apps/group/urls.py

from django.urls import path
from .views import manage_groups

urlpatterns = [
    path('group_update', manage_groups, name='manage_groups'),
    path('<int:group_id>/', manage_groups, name='update_group'),
]
