from django.urls import path
from . import views
from django.conf import settings          #! Importanteeeee importar

# Creamos el archivo URLs del core aqui para no saturar el global

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('sample/', views.sample, name='sample'),
]

if settings.DEBUG:         #! IMPORTANTE
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)