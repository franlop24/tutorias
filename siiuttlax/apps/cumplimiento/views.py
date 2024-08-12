from django.shortcuts import render, get_object_or_404
from apps.period.models import Period
from apps.group.models import Group
from apps.reporte_tutoria.models import ReporteTutoria
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    periods = Period.objects.all()
    current_period = None  
    grupos_data = []
    
    if 'periodo' in request.GET:
        periodo_id = request.GET.get('periodo')
        current_period = get_object_or_404(Period, id=periodo_id)
        grupos = Group.objects.filter(period=current_period)
    
    return render(request, 'cumplimiento/consultas.html', {'periods': periods, 'current_period': current_period, 'grupos': grupos_data})

@login_required
def consultas_por_periodo(request, periodo_id):
    period = get_object_or_404(Period, id=periodo_id)
    grupos = Group.objects.filter(period=period)
    
    # Determinar los meses incluidos en el periodo seleccionado
    period_months = {
        'Enero - Abril': [1, 2, 3, 4],
        'Mayo - Agosto': [5, 6, 7, 8],
        'Septiembre - Diciembre': [9, 10, 11, 12]
    }
    months_available = period_months.get(period.period, [])
    
    # Obtener el mes del parámetro GET, si existe
    mes = request.GET.get('mes', None)
    
    grupos_data = []
    num_actividades_esperadas = 4
    
    for grupo in grupos:
        actividades = ReporteTutoria.objects.filter(grupo=grupo)
        
        # Filtrar reportes por mes solo si se selecciona un mes válido
        if mes and int(mes) in months_available:
            actividades = actividades.filter(fecha_tutoria__month=int(mes))
        
        actividades_data = []
        
        for actividad in actividades:
            actividades_data.append({
                'nombre_actividad': actividad.nombre_actividad,
                'evidencia_lista_asistencia': actividad.evidencia_lista_asistencia.url if actividad.evidencia_lista_asistencia else None,
                'evidencia_canalizacion_alumno': actividad.evidencia_canalizacion_alumno.url if actividad.evidencia_canalizacion_alumno else None
            })
        
        # Completar con actividades "No reportado" si faltan
        actividades_completas = actividades_data + [{'nombre_actividad': 'No reportado', 'evidencia_lista_asistencia': None, 'evidencia_canalizacion_alumno': None}] * (num_actividades_esperadas - len(actividades_data))
        
        # Mostrar el grupo si tiene actividades o si no se ha seleccionado un mes
        if not mes or actividades_data:
            grupos_data.append({
                'Cuatrimestre': grupo.semester.semester_name,
                'Grupo': grupo.group,
                'Tutor': grupo.tutor.full_name if grupo.tutor else 'No asignado',
                'Periodo': str(grupo.period),
                'Carrera': grupo.career.short_name if grupo.career else 'No asignada',
                'Actividades': actividades_completas
            })

    periods = Period.objects.all()
    return render(request, 'cumplimiento/consultas.html', {
        'grupos': grupos_data,
        'current_period': period,
        'periods': periods,
        'selected_mes': mes,
        'months_available': months_available
    })
