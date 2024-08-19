# views.py
from django.shortcuts import render, redirect
from .forms import VAKInterviewForm, HEInterviewForm
from .models import VAKInterview, HEInterview, VAKResults, HEResults
from django.contrib.auth.decorators import login_required

@login_required
def fill_testv_interview(request):
    student = request.user.student
    
    if request.method == 'POST':
        form = VAKInterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.student = student
            interview.save()
            
            # Actualizar los resultados de VAKResults
            results, created = VAKResults.objects.get_or_create(student=student)
            results.update_counts()
            
            return redirect('student_dashboard')
    else:
        form = VAKInterviewForm()
    
    return render(request, 'interview/test_v_form.html', {'form': form})


@login_required
def fill_testhe_interview(request):
    student = request.user.student
    
    if request.method == 'POST':
        form = HEInterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.student = student
            interview.save()

            results, created = HEResults.objects.get_or_create(student=student)
            results.update_counts()
            
            return redirect('student_dashboard')
    else:
        form = HEInterviewForm()
    
    return render(request, 'interview/test_he_form.html', {'form': form})