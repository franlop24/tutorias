from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import JustificanteForm, ProfesoresArchivosForm
from .models import Justificante
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

class CustomLoginView(LoginView):
    template_name = 'justify/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse('ruta_tutor') 
        else:
            return reverse('ruta_alumno')

def alumno_view(request):
    if request.method == 'POST':
        justificante_form = JustificanteForm(request.POST)
        profesores_archivos_form = ProfesoresArchivosForm(request.POST, request.FILES)
        
        if justificante_form.is_valid() and profesores_archivos_form.is_valid():
            justificante = justificante_form.save(commit=False)
            justificante.fecha = timezone.now().date()
            justificante.anio = justificante.fecha.year
            justificante.mes = justificante.fecha.strftime('%B')
            justificante.save()
            profesores_archivos_form.instance = justificante
            profesores_archivos_form.save()
            messages.success(request, 'Justificante enviado correctamente.')
            return redirect('ruta_alumno')
    else:
        now = timezone.now()
        justificante_form = JustificanteForm(initial={
            'fecha': now.day,
            'mes': now.strftime('%B'),
            'anio': now.year
        })
        profesores_archivos_form = ProfesoresArchivosForm()
    
    return render(request, 'justify/solicitar_justificante.html', {
        'justificante_form': justificante_form,
        'profesores_archivos_form': profesores_archivos_form
    })
def tutor_view(request):
    justificantes = Justificante.objects.all()  
    return render(request, 'justify/revisar_justificantes.html', {'justificantes': justificantes})

def revisar_justificante_view(request, justificante_id):
    justificante = get_object_or_404(Justificante, id=justificante_id)
    if request.method == 'POST':
        if 'aceptar' in request.POST:
            justificante.estado = 'Aceptado'
            justificante.save()
            messages.success(request, 'Justificante aceptado.')
            return redirect('ruta_tutor')  
        elif 'rechazar' in request.POST:
            justificante.estado = 'Rechazado'
            justificante.save()
            messages.success(request, 'Justificante rechazado.')
            return redirect('ruta_tutor')  
    return render(request, 'justify/detalle_justificante.html', {'justificante': justificante})