from django.contrib import admin

# Register your models here.

from .models import VAKInterview

@admin.register(VAKInterview)
class VAKInterviewAdmin(admin.ModelAdmin):
    list_display = ('student', 'interview_date')

    