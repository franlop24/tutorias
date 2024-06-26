# views.py

from django.shortcuts import render, redirect
from .forms import InitialInterviewForm
from .models import InitialInterview
from django.contrib.auth.decorators import login_required

@login_required
def fill_initial_interview(request):
    student = request.user.student
    
    if request.method == 'POST':
        form = InitialInterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.student = student
            interview.save()
            return redirect('student_dashboard')  # Puedes redirigir a donde corresponda después de guardar
    else:
        form = InitialInterviewForm()
    
    return render(request, 'interview/initial_interview_form.html', {'form': form})
