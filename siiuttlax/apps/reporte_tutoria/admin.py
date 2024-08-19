from django.contrib import admin
from .models import ReporteTutoria
# Register your models here.

class Reportes_Tutorias(admin.ModelAdmin):
    fields = ["fecha_tutoria",
              "carrera","semestre",
              "grupo",
              "nombre_actividad",
              "objetivo_actividad",
              "descripcion_actividad",
              "evidencia_fotografica",
              "evidencia_lista_asistencia",
              "evidencia_audio",
              "evidencia_canalizacion_alumno",
              "tutor"]
    list_display = ["fecha_tutoria", "tutor"]

admin.site.register(ReporteTutoria, Reportes_Tutorias)
    