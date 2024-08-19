# forms.py

from django import forms
from .models import InitialInterview

class InitialInterviewForm(forms.ModelForm):
    class Meta:
        model = InitialInterview
        exclude = ['student', 'active']  # Excluye 'active' del formulario
        widgets = {
            'interview_date': forms.DateInput(attrs={'type': 'date'}),
        }
