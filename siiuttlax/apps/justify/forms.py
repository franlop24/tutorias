from django import forms
from .models import Justificante, Usuario
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth.models import User 

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']

from django import forms
from .models import Justificante

class JustificanteForm(forms.ModelForm):
    nivel = forms.ChoiceField(choices=[('TSU', 'TSU'), ('Ingeniería', 'Ingeniería')], widget=forms.RadioSelect())

    class Meta:
        model = Justificante
        fields = ['alumno', 'grupo', 'carrera', 'nivel', 'dias_falta', 'mes', 'motivo']
        widgets = {
            'alumno': forms.TextInput(attrs={'placeholder': 'Nombre Completo'}),
            'grupo': forms.TextInput(attrs={'placeholder': 'Grupo'}),
            'carrera': forms.TextInput(attrs={'placeholder': 'Carrera'}),
            'dias_falta': forms.TextInput(attrs={'placeholder': 'Ingrese la fecha o fechas separadas por coma'}),
            'mes': forms.TextInput(attrs={'placeholder': 'Mes'}),
            'motivo': forms.TextInput(attrs={'placeholder': 'Motivo'}),
        }

class ProfesoresArchivosForm(forms.ModelForm):
    profesores = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_staff=True), widget=forms.CheckboxSelectMultiple())
    adjuntar_archivos = forms.FileField(required=False, widget=forms.FileInput())

    class Meta:
        model = Justificante
        fields = ['profesores', 'adjuntar_archivos']