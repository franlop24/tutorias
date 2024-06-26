from django.contrib import admin

from .models import Admin, Professor, Student

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'username', 'email', 'employee_number', 'title')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'username', 'email', 'enrollment')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    fields = ('first_name', 'username', 'email',)