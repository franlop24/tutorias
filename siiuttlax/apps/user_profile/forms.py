# apps/user_profile/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileUpdateForm(UserChangeForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    enrollment = forms.CharField(label="Matrícula", required=False)
    last_name_father = forms.CharField(label="Apellido Paterno", max_length=30, required=True)
    last_name_mother = forms.CharField(label="Apellido Materno", max_length=30, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ocultar campos no deseados
        if 'is_superuser' in self.fields:
            self.fields['is_superuser'].widget = forms.HiddenInput()
        if 'is_staff' in self.fields:
            self.fields['is_staff'].widget = forms.HiddenInput()
        if 'groups' in self.fields:
            self.fields['groups'].widget = forms.HiddenInput()
        if 'user_permissions' in self.fields:
            self.fields['user_permissions'].widget = forms.HiddenInput()
        
        # Ocultar el campo de matrícula si el usuario no es estudiante
        if not hasattr(self.instance, 'student'):
            self.fields['enrollment'].widget = forms.HiddenInput()

        # Divide el campo last_name en last_name_father y last_name_mother
        if self.instance.last_name:
            last_names = self.instance.last_name.split(' ')
            if len(last_names) >= 2:
                self.initial['last_name_father'] = last_names[0]
                self.initial['last_name_mother'] = ' '.join(last_names[1:])

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            return password  # Devuelve la nueva contraseña si se proporcionó
        return self.instance.password  # Devuelve la contraseña actual si no se proporcionó una nueva

    def save(self, commit=True):
        user = super().save(commit=False)
        # Combina los apellidos paterno y materno en el campo last_name
        user.last_name = f"{self.cleaned_data['last_name_father']} {self.cleaned_data['last_name_mother']}"
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name_father', 'last_name_mother', 'email', 'password', 'enrollment']


# apps/academy/forms.py

from django import forms
from .models import Profile
from datetime import date

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biography', 'sexo', 'age', 'fecha_nacimiento', 'lugar_nacimiento', 'direccion', 'celular', 'telefono_emergencia', 'numero_seguro_social', 'tipo_sangre']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
             'age': forms.HiddenInput(),  
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_nacimiento = cleaned_data.get("fecha_nacimiento")

        if fecha_nacimiento:
            today = date.today()
            age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            cleaned_data['age'] = age

        return cleaned_data








