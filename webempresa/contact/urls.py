from django.urls import path
from . import views
from django.conf import settings          #! Importanteeeee importar

# Creamos el archivo URLs del core aqui para no saturar el global

urlpatterns = [
    path('/', views.contact, name='contact'),
]

if settings.DEBUG:         #! IMPORTANTE
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)