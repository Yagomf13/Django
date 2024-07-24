from django.shortcuts import render

html_base = """
<h1>Mi Web Personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contacto/">Contacto</a></li>
</ul>
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, 'core/about-me.html')

def contacto(request):
    return render(request, 'core/contacto.html')