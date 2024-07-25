from django.shortcuts import render, redirect
from django.urls import reverse          #! Para no poner las urls en crudo 
from .forms import ContactForm

# Create your views here.
def contact(request):
    # print("Tipo de petición: {}".format(request.method))          #!Te da el tipo de petición

    contact_form = ContactForm        #!Se crea la plantilla vacia
    
    if request.method == 'POST':        #! Verificamos si el formulario es tipo Post
        contact_form = ContactForm(data=request.POST)       #!Volvemos a guardar los datos en contact_form e incluye los datos del formulario
        if contact_form.is_valid():         #!Si el formulario es valido
            name = request.POST.get('name', '')      #! Obtenemos los datos del formulario
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Se supone que todo ha ido bien por lo tanto redireccionamos
            return redirect(reverse('contact')+'ok')

    
    return render(request, 'contact/contact.html', {'form': contact_form})