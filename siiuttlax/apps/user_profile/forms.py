# apps/user_profile/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

# forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from apps.academy.models import Student

User = get_user_model()

class ProfileUpdateForm(UserChangeForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    enrollment = forms.CharField(label="Matrícula", required=False)

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

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            return password  # Devuelve la nueva contraseña si se proporcionó
        return self.instance.password  # Devuelve la contraseña actual si no se proporcionó una nueva

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'enrollment']

# apps/academy/forms.py

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biography', 'sexo', 'age', 'fecha_nacimiento', 'lugar_nacimiento', 'direccion', 'celular', 'telefono_emergencia', 'numero_seguro_social', 'tipo_sangre']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }







