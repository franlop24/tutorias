#models.py
from django.db import models
from apps.academy.models import Student

class VAKInterview(models.Model):
    RESPUESTAS_V_CHOICES = [
        ('Verdadero', 'Verdadero'),
        ('Falso', 'Falso')
    ]

    student = models.OneToOneField(Student, blank=True, null=True, on_delete=models.CASCADE, related_name='vak_interview')
    interview_date = models.DateField(blank=True, null=True, verbose_name='Fecha de la entrevista')

    C1= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Prefieres hacer un mapa que explicarle a alguien como tiene que llegar.')
    F2= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Si estoy enojad0(a) o contento(a) generalmente se exactamente por qué.')
    E3= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Se tocar (o antes sabia tocar) un instrumento musical.')
    E4= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Asocio la musica con mis estados de animo.')
    B5= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Se sumar o multiplicar mentalmente con mucha rapidez.')
    F6= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Puedo ayudar a un amigo a manejar sus sentimientos porque yo lo pude hacer antes en relacion a sentimientos parecidos.')
    B7= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me gusta trabajar con calculadoras e computadores.')
    D8= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Aprendo rapido a bailar un ritmo nuevo.')
    A9= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='No me es dificil decir lo que pienso en el curso de uns discusion o debate.')
    A10= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Disfruto de una buena charla, discuso o sermon.')
    C11= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Siempre distingo el norte del sur, este donde este.')
    G12= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me gusta reunir grupos de personas en una fiesta o en un evento especial.')
    E13= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='La vida me parece vacia sin la musica.')
    C14= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Siempre entiendo los graficos que vienen en instrucciones de equipos o instrumentos.')
    B15= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me gusta hacer rompecabezas y entretenerme con juegos electronicos.')
    D16= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me fue facil aprender a andar en bicicleta(o patines).')
    A17= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me enojo cuando oigo una discusion o una afrimacion que parece ilogica.')
    G18= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Soy capaz de convencer a otros que sigan mis planes.')
    D19= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Tengo un buen sentido del equilibrio y coordinacion.')
    B20= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Con frecuencia veo configuraciones y relaciones entre numeros con mas rapidez y facilidad que otros.')
    D21= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me gusta construir modelos(o hacer esculturas).')
    A22= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Tengo agudeza para encontrar significado en las palabras.')
    C23= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Puedo mirar un objeto de una manera y con a misma facilidad verlo.')
    E24= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Con freciencia hago conexion entre una pieza de musica y algun evento de mi vida.')
    B25= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me gusta trabajar con numeros y figuras.')
    F26= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me gusta sentarme sileciosamente y refleccionar sobre mis sentimientos intimos.')
    C27= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Con solo mirar la forma de construcciones y estructuras me siento a gusto.')
    E28= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me gusta tararear, silbar y cantar en la ducha o cuando estoy solo(a).')
    D29= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Soy bueno para el atletismo.')
    A30= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me gusta escribir cartas detalladas a mis amigos.')
    F31= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Generalmente me doy cuenta de la expresion que tengo en la cara.')
    G32= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me doy cuenta de las expresiones en la cara de otras personas.')
    F33= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me mantengo "en contacto" con mis estados de animo. No me cuesta identificarlos.')
    G34= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me doy cuenta de los estados de animo de los otros.')
    G35= models.CharField(max_length=10, choices=RESPUESTAS_V_CHOICES, blank=True, null=True, verbose_name='Me doy cuenta bastante bien de lo que otros piensan de mi.')

    class Meta:
        verbose_name = 'Test de Inteligencia Multiple'
        verbose_name_plural = 'Test de Inteligencias Multiples'

class HEInterview(models.Model):

    RESPUESTAS_HE_CHOICES = [
        ('Si', 'Si'),
        ('No', 'No')
    ]

    student = models.OneToOneField(Student, blank=True, null=True, on_delete=models.CASCADE, related_name='he_interview')
    interview_date = models.DateField(blank=True, null=True, verbose_name='Fecha de la entrevista')

    HE1 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Trabajas siempre en el mismo lugar?')
    HE2 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿El lugar que tienes para estudiar esta aislado de ruido?')
    HE3 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Te cuesta trabajo concentarte para estudiar?')
    HE4 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿El lugar donde estudias tiene buena iluminacion(Luz natural o artificial a la hora de estudiar)?')
    HE5 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Tiene tu habitacion limpieza, orden y buena iluminacion?')
    HE6 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿La temperatura del lugar donde estudias se encuentra entre los 20° a 22° grados?')
    HE7 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Te gusta estudiar con la ventana abierta o entreabierta?')
    HE8 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Cuándo empiezas a estudiar, tienes a mano todo el material necesario? (Libros, diccionario, etcétera).')
    HE9 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Estudias en una silla de respaldo que permita sentarte apoyando bien tu espalda, sin posturas defectuosas?')
    HE10 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Tu silla es proporcionada en altura a la mesa de trabajo?')
    HE11 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Cuentas con una agenda o calendario para administrar tu tiempo?')
    HE12 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Tienes un horario fijo para estudiar y descansar?')
    HE13 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Has realizado una planificación anotando el tiempo que debes de dedicar a tu estudio diariamente?')
    HE14 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Tu planificación ¿Incluye el tiempo estimado que emplearas en el estudio de todas las asignaturas?')
    HE15 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Incluyes períodos de descanso en tu plan de estudio?')
    HE16 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Estudias al menos 5 días por semana?')
    HE17 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Antes de comenzar y antes de estudiar ¿Determinas tu plan de trabajo y el tiempo que vas a tardar en demorar en realizarlo?')
    HE18 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Realizas primero los trabajos más difíciles que los fáciles?')
    HE19 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Acudes diariamente a todas las clases?')
    HE20 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Miras con interés al profesor cuando explica?')
    HE21 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Anotas las tareas que debes de realizar en tu casa?')
    HE22 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Realizas las tareas que te asignan tus docentes?')
    HE23 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Atiendes al profesor, tratando de entender todo lo que dice?')
    HE24 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Preguntas cuando hay algo que no entiendes?')
    HE25 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Tu profesor te motiva a estudiar o repasar lo visto en clase?')
    HE26 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Tu profesor te motiva a investigar más de los temas vistos en clases?')
    HE27 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Prefieres trabajar solo cuando tienes que realizar alguna actividad en clase o fuera de la escuela?')
    HE28 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Participas en actividades de grupo en el salón de clase?')
    HE29 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Tomas apuntes de lo que los profesores explican?')
    HE30 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Antes de tomar apuntes ¿Escribes la fecha y el título del tema?')
    HE31 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Escribes en todas las asignaturas?')
    HE32 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Tu profesor te motiva?')
    HE33 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Utilizas lápiz de color para destacar lo más importante?')
    HE34 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Anotas las palabras extrañas y lo que no comprendes?')
    HE35 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Revisas y completas tus apuntes con otro compañero?')
    HE36 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Acostumbras a mirar el índice de un texto antes de empezar a estudiar?')
    HE37 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Realizar una lectura rápida del texto, previo al estudio más detallado?')
    HE38 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Te apoyas de los apuntes tomados en clase para estudiar una asignatura?')
    HE39 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Identificas las ideas principales de los textos?')
    HE40 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Subrayas las ideas principales de los textos?')
    HE41 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Cuándo tienes distintas fuentes de información para un mismo tema ¿Haces un resumen para terminar con una síntesis general?')
    HE42 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Utilizas en tu estudio habitual técnicas como el esquema, cuadros, gráficos etcétera?')
    HE43 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Acostumbras a memorizar las ideas principales de un tema?')
    HE44 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Utilizas las fichas de estudio para memorizar alguna fecha, número, datos concretos o vocabulario?')
    HE45 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Utilizas el diccionario para aclarar tus ideas con respecto a una palabra, tanto para su significado como para su ortografía?')
    HE46 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Marcas lo que no comprendes?')
    HE47 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Escribes los datos importantes que te son difíciles para recordar?')
    HE48 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Utilizas alguna técnica para memorizar estos datos?')
    HE49 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Repasas las materias?')
    HE50 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Pides ayuda a tus profesores, compañeros o padres, cuando tienes dificultades en tus estudios?')
    HE51 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Mantienes tus cuadernos y tareas al día?')
    HE52 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Entregas a tiempo tus tareas, trabajos, etcétera?')
    HE53 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Cumples con la planificación de estudio que te has propuesto para una sesión de trabajo?')
    HE54 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Haces esquemas de las asignaturas que no comprendes los temas vistos en clases?')
    HE55 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Al realizar los esquemas ¿Consideras tus propios apuntes?')
    HE56 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Utilizas los esquemas para facilitar la comprensión de los temas más fáciles?')
    HE57 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Destacas las ideas principales al hacer tus esquemas?')
    HE58 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Respetas la “sangría” para comenzar un párrafo?')
    HE59 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Consultas otros libros además de tu texto de estudio?')
    HE60 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Redactas tus trabajos en forma clara, coherente y concisa?')
    HE61 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Revisas la ortografía, redacción, y limpieza en tus trabajos?')
    HE62 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Te gusta estudiar?')
    HE63 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Tienes clara las razones por las que estudias?')
    HE64 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿El estudio es para ti un medio para aprender?')
    HE65 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Te gusta lo que aprendes con tus docentes?')
    HE66 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Logras una buena concentración desde el comienzo de tu sesión de estudio?')
    HE67 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Cuando faltas a clase ¿Procuras informarte de lo que se ha realizado y de lo que se va a realizar?')
    HE68 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Piensas que las personas deben estudiar para aprender y no sólo para aprobar una asignatura?')
    HE69 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Estudias antes de presentar un examen?')
    HE70 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Presentas tu examen solo con los conocimientos que posees?')
    HE71 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Cuándo te has sacado una mala nota, intentas superar tu estado de ánimo continuando con interés en las materias?')
    HE72 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Tratas de entregar lo máximo de ti para obtener un buen resultado escolar?')
    HE73 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Utilizas alguna técnica de relajación para reducir la ansiedad antes o durante los exámenes?')
    HE74 = models.CharField(max_length=10, choices=RESPUESTAS_HE_CHOICES, blank=True, null=True, verbose_name='¿Estás satisfecho con tus resultados escolares?')

    class Meta:
        verbose_name = 'Test de Habito de Estudio'
        verbose_name_plural = 'Test de Habitos de Estudios'
        #Añadir los modulos de respuestas 

class VAKResults(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='vak_results')
    count_A = models.IntegerField(default=0)
    count_B = models.IntegerField(default=0)
    count_C = models.IntegerField(default=0)
    count_D = models.IntegerField(default=0)
    count_E = models.IntegerField(default=0)
    count_F = models.IntegerField(default=0)
    count_G = models.IntegerField(default=0)

    def update_counts(self):
        interview = self.student.vak_interview
        if not interview:
            return

        self.count_A = sum(1 for field in ['A9', 'A10', 'A17', 'A22', 'A30'] if getattr(interview, field) == 'Verdadero')
        self.count_B = sum(1 for field in ['B5', 'B7', 'B15', 'B20', 'B25'] if getattr(interview, field) == 'Verdadero')
        self.count_C = sum(1 for field in ['C1', 'C11', 'C14', 'C23', 'C27'] if getattr(interview, field) == 'Verdadero')
        self.count_D = sum(1 for field in ['D8', 'D16', 'D19', 'D21', 'D29'] if getattr(interview, field) == 'Verdadero')
        self.count_E = sum(1 for field in ['E3', 'E4', 'E13', 'E24', 'E28'] if getattr(interview, field) == 'Verdadero')
        self.count_F = sum(1 for field in ['F2', 'F6', 'F26', 'F31', 'F33'] if getattr(interview, field) == 'Verdadero')
        self.count_G = sum(1 for field in ['G12', 'G18', 'G32', 'G34', 'G35'] if getattr(interview, field) == 'Verdadero')
        self.save()

    def _str_(self):
        return f'Resultados de {self.student}'

    class Meta:
        verbose_name = 'Resultado de VAK'
        verbose_name_plural = 'Resultados de VAK'

class HEResults(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='he_results')
    contadorHE = models.IntegerField(default=0)

    def update_counts(self):
        interview = self.students.he_interview
        if not interview:
            return
        
        self.contadorHE = sum(1 for field in [ 
        'HE1', 'HE2', 'HE3', 'HE4', 'HE5', 'HE6', 'HE7', 'HE8', 'HE9', 'HE10',
        'HE11', 'HE12', 'HE13', 'HE14', 'HE15', 'HE16', 'HE17', 'HE18', 'HE19', 'HE20',
        'HE21', 'HE22', 'HE23', 'HE24', 'HE25', 'HE26', 'HE27', 'HE28', 'HE29', 'HE30',
        'HE31', 'HE32', 'HE33', 'HE34', 'HE35', 'HE36', 'HE37', 'HE38', 'HE39', 'HE40',
        'HE41', 'HE42', 'HE43', 'HE44', 'HE45', 'HE46', 'HE47', 'HE48', 'HE49', 'HE50',
        'HE51', 'HE52', 'HE53', 'HE54', 'HE55', 'HE56', 'HE57', 'HE58', 'HE59', 'HE60',
        'HE61', 'HE62', 'HE63', 'HE64', 'HE65', 'HE66', 'HE67', 'HE68', 'HE69', 'HE70',
        'HE71', 'HE72', 'HE73', 'HE74'] if getattr(interview, field) == 'Si')
        self.save()

    def _str_(self):
        return f'Resultados de {self.student}'
    
    class Meta:
        verbose_name = 'Resultado de HE'
        verbose_name_plural = 'Resultados de HE'