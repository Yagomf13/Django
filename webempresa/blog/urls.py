from django.urls import path
from . import views

# Creamos el archivo URLs del core aqui para no saturar el global

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.category, name='category')  #!Campo dinamico que depende de la id y lo pone en entero
]