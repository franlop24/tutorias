from django.contrib import admin
from .models import InitialInterview

@admin.register(InitialInterview)
class InitialInterviewAdmin(admin.ModelAdmin):
    list_display = ('student', 'interview_date')
