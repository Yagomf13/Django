from django.shortcuts import render
from .models import Project


# Create your views here.
def portfolio(request):               #definimos aqui porque es app propia
    projects = Project.objects.all()  #obtenemos todos los proyectos
    return render(request, 'portfolio/portfolio.html', {'projects': projects})  #diccionario de contexto que es un nombre para cada variable que enviemos al template