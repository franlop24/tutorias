# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Professor, Admin

class StudentRegistrationForm(UserCreationForm):
    enrollment = forms.CharField(required=False, max_length=12, label='Matrícula')
    last_name_father = forms.CharField(max_length=30, label='Apellido Paterno')
    last_name_mother = forms.CharField(max_length=30, label='Apellido Materno')

    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name_father', 'last_name_mother', 'email', 'enrollment', 'password1', 'password2']


class ProfessorForm(forms.ModelForm):
    last_name_father = forms.CharField(max_length=30, label='Apellido Paterno')
    last_name_mother = forms.CharField(max_length=30, label='Apellido Materno')

    class Meta:
        model = Professor
        fields = ['username', 'first_name', 'last_name_father', 'last_name_mother', 'email', 'password', 'title', 'employee_number']
        widgets = {
            'password': forms.PasswordInput(),
        }


class AdminForm(UserCreationForm):
    last_name_father = forms.CharField(max_length=30, label='Apellido Paterno')
    last_name_mother = forms.CharField(max_length=30, label='Apellido Materno')

    class Meta:
        model = Admin
        fields = ['username', 'first_name', 'last_name_father', 'last_name_mother', 'email', 'password1', 'password2']
