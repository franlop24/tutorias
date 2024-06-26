# forms.py

from django import forms
from .models import InitialInterview

class InitialInterviewForm(forms.ModelForm):
    class Meta:
        model = InitialInterview
        exclude = ['student']  # Excluye el campo 'student' ya que lo asignaremos manualmente en la vista
        widgets = {
            'interview_date': forms.DateInput(attrs={'type': 'date'}),
        }
