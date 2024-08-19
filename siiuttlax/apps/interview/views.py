from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import InitialInterviewForm
from .models import InitialInterview

@login_required
def fill_initial_interview(request):
    student = request.user.student
    interview = InitialInterview.objects.filter(student=student).first()

    if interview and not interview.active:
        # Permitir la visualización de la entrevista completada
        form = InitialInterviewForm(instance=interview)
        for field in form.fields:
            form.fields[field].widget.attrs['readonly'] = True  # Hacer campos de solo lectura
        return render(request, 'interview/initial_interview_form.html', {
            'form': form,
            'interview_exists': True,
            'interview_active': False
        })

    if request.method == 'POST':
        form = InitialInterviewForm(request.POST, instance=interview)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.student = student
            interview.active = False  # Desactivar la entrevista una vez completada
            interview.save()
            messages.success(request, 'Entrevista inicial guardada correctamente.')
            return redirect('student_dashboard')
    else:
        form = InitialInterviewForm(instance=interview)

    return render(request, 'interview/initial_interview_form.html', {
        'form': form,
        'interview_exists': bool(interview),
        'interview_active': interview.active if interview else True
    })
