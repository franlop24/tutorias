from django.db import models
from django.contrib.auth.models import User
from apps.career.models import Career
from apps.library.models import Module, Question
# Create your models here.

# class Stage (models.Model):
#     stage = models.IntegerField(
#         verbose_name = "Etapa",)
#     application_date = models.DateField(
#         verbose_name = "Fecha de aplicacion",
#     )

#     @property
#     def year(self):
#         return self.application_date.year
#     @property
#     def month(self):
#         months = ['enero', 'febrero', 'marzo',
#                  'abril', 'mayo', 'junio', 'julio',
#                  'agosto', 'septiembre', 'octubre',
#                  'noviembre', 'diciembre']
#         return months[self.application_date.month -1 ]
    
#     def __str__(self):
#         return f"{self.stage} - {self.month }-{self.year}"
    
#     class Meta:
#         verbose_name = "etapa"
#         verbose_name_plural = "etapas"

class Exam(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        verbose_name = "Usuario"
    )

    modules  = models.ManyToManyField(
        Module,
        through='ExamModule',
        verbose_name ="Módulos"
        )
    questions = models.ManyToManyField(
        Question,
        through='Breakdown',
        verbose_name='Preguntas'
    )
    score = models.FloatField(
        verbose_name ="Calificacion",
        default = 0.0
    )
    created = models.DateTimeField(
        verbose_name = 'Fecha de creacion',
        auto_now_add =True
    )
    updated = models.DateTimeField(
        verbose_name = 'Fecha de actualizacion',
        auto_now =True
        )

    def set_modules(self):
        for module in Module.objects.all():
            self.modules.add(module)

    def set_questions(self):
        for module in self.modules.all():
            for question in Question.objects.filter(module=module):
             Breakdown.objects.create(
                 exam = self,
                 question = question,
                 correct = question.correct,
            )
    def compute_score(self):
        score = 0.0
        total_questions = 0
        for breakdown in self.breakdown_set.all():
            total_questions += 1
            if breakdown.answer == breakdown.correct:
                score += 1

        self.score = score / total_questions if total_questions > 0 else 0
        self.save()

    def compute_score_by_module(self, m_id):
        score = 0.0
        for question in self.breakdown_set.filter(question__module_id=m_id):
            if question.answer == question.correct:
                score += 1

        module = self.exammodule_set.get(module_id=m_id)
        module.score = score
        module.save()

    def __str__(self):
        return f"{self.user}: {self.score}"
    
    class Meta:
        verbose_name = "examen"
        verbose_name_plural = "examenes"

class ExamModule(models.Model):
    exam = models.ForeignKey(
        Exam,
        on_delete= models.CASCADE,
        verbose_name= "Examen"
        )
    module = models.ForeignKey(
        Module,
        on_delete= models.CASCADE,
        verbose_name= "Módulo"
        )
    active = models.BooleanField(
        verbose_name= "Activo",
        default= True,
        )
    score = models.FloatField(
        verbose_name= "Calificación",
        default= 0.0
        )
    
    def __str__(self):
        return f"{self.module} - {self.score}"
    
    @property
    def total_questions(self):
        return self.module.question_set.count()
    
class Breakdown(models.Model):
    exam = models.ForeignKey(
        Exam,
        on_delete = models.CASCADE,
        verbose_name = "Examen"
    )
    question = models.ForeignKey(
        Question,
        on_delete = models.CASCADE,
        verbose_name='Pregunta'
    )
        
    answer = models.CharField(
         verbose_name =' Respuesta',
         max_length = 5,
         default = '-'
    )
    
    correct = models.CharField(
        verbose_name = 'Respuesta correcta',
        max_length = 5,
        default = '-'
    )

    def __str__(self):
        return f"{self.question} - {self.answer}: {self.correct}"