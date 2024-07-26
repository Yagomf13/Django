from django.shortcuts import render, redirect
from django.urls import reverse                          #! Para no poner las urls en crudo 
from django.core.mail import EmailMessage                #! Sirve para enviar los correos
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

            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',                       #Asunto
                'De {} <{}>\n\nEscribio:\n\n{}'.format(name, email, content),      #Cuerpo del mensaje
                'no-contestar@inbox.mailtrap.io',                                  #Email de orige
                ['yagomf13@gmail.com'],                                            #Email de destino
                reply_to={email}                                                   #A quien contestar
            )

            try:
                email.send()
                    # Ha ido bien redireccionamos a ok 
                return redirect(reverse('contact')+'?ok') #! Redirige a la pagina conforme se ha enviado correctamente
            except:
                    # Algo no ha ido bien redireccionamos a FAIL
                return redirect(reverse('contact')+'?fail') #! Redirige a la pagina conforme no se ha enviado

    
    return render(request, 'contact/contact.html', {'form': contact_form})