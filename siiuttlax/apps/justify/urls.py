from django.urls import path
from .views import alumno_view, revisar_justificante_view, tutor_view, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('solicitar/', alumno_view, name='ruta_alumno'),
    path('revisar/', tutor_view, name='ruta_tutor'),
        path('revisar/justificante/<int:justificante_id>/', revisar_justificante_view, name='ruta_para_revisar_justificante'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)