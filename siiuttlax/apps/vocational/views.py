import random
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import Breakdown, Exam
from django.contrib.auth.decorators  import login_required

# Create your views here.

@login_required
def home(request):
    user = request.user
    if user.is_superuser:
        return redirect('admin:index')
    return render(request, 'home/home.html', {'user': user})

@login_required
def test(request, q_id=1):

    try:  
        exam = request.user.exam
    except:
        exam = Exam.objects.create(
                user=request.user)
        exam.set_modules()
        exam.set_questions()

    # Obtener todas las preguntas de todos los módulos
    questions = list(Breakdown.objects.filter(exam=exam))

    # Barajar las preguntas si es la primera pregunta
    if q_id == 1:
        random.shuffle(questions)
        request.session['questions'] = [q.id for q in questions]

    # Obtener la pregunta actual
    questions_ids = request.session.get('questions')
    current_question = get_object_or_404(Breakdown, id=questions_ids[q_id - 1])

    if request.method == 'POST':
        answer = request.POST['answer']
        current_question.answer = answer
        current_question.save()

        if q_id < len(questions):
            return redirect('vocational:test', q_id=q_id + 1)
        else:
            exam.compute_score()
            # Calcular la puntuación por módulo
            for module in exam.modules.all():
                exam.compute_score_by_module(module.id)
            return redirect('vocational:results')

    return render(request, 'vocational/test.html', {
        'question': current_question.question,
        'answer': current_question.answer,
        'q_id': q_id,
        'total_questions': len(questions),
    })

@login_required
def results(request):
    exam = request.user.exam
    modules = exam.exammodule_set.all().order_by('-score')
    return render(request, 'vocational/results.html', {'modules': modules})
