# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentRegistrationForm(UserCreationForm):
    enrollment = forms.CharField(required=False, max_length=12, label='Matrícula')

    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email', 'enrollment', 'password1', 'password2']

from django import forms
from .models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'title', 'employee_number']
        widgets = {
            'password': forms.PasswordInput(),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Admin

class AdminForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']




