from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def sample(request):
    return render(request, "core/sample.html")