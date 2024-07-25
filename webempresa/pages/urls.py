from django.urls import path
from . import views

# Creamos el archivo URLs del core aqui para no saturar el global

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page')  #!Campo dinamico que depende de la id y lo pone en entero
]