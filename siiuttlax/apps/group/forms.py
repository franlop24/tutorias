# apps/group/forms.py

from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['semester', 'group', 'observations', 'period', 'career', 'tutor']
