# forms.py
from django import forms
from .models import VAKInterview, HEInterview, VAKResults, HEResults

class VAKInterviewForm(forms.ModelForm):
    class Meta:
        model = VAKInterview
        exclude = ['student']  # Excluye el campo 'student' ya que lo asignaremos manualmente en la vista
        widgets = {
            'interview_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            if instance.student:
                results, created = VAKResults.objects.get_or_create(student=instance.student)
                results.update_counts()
        return instance

class HEInterviewForm(forms.ModelForm):
    class Meta:
        model = HEInterview
        exclude = ['student']
        widgets = {
            'he_interview_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            if instance.student:
                results, created = HEResults.objects.get_or_create(student=instance.student)
                results.update_counts()
        return instance