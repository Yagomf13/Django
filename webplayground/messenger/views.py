from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread, Message
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ThreadList(TemplateView):
    template_name = 'messenger/thread_list.html'

class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj
    
def add_message(request, pk):
    # Inicializa un diccionario de respuesta JSON con una clave 'created' que inicialmente es False.
    json_response = {'created': False}
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Obtiene el contenido del mensaje desde los parámetros GET de la solicitud
        content = request.GET.get('content', None)
        # Si el contenido no es None (es decir, si se envió algún mensaje)
        if content:
            # Intenta obtener el objeto Thread con la clave primaria pk, o lanza un error 404 si no se encuentra
            thread = get_object_or_404(Thread, pk=pk)
            # Crea un nuevo mensaje con el usuario autenticado y el contenido proporcionado
            message = Message.objects.create(user=request.user, content=content)
            # Añade el mensaje recién creado al hilo (thread) encontrado
            thread.messages.add(message)
            # Actualiza el diccionario de respuesta JSON indicando que el mensaje fue creado con éxito
            json_response['created'] = True
            if len(thread.messages.all()) is 1:
                json_response['first'] = True
    # Si el usuario no está autenticado, lanza un error 404 con un mensaje personalizado
    else:
        raise Http404('User is not authenticated')
    # Retorna una respuesta JSON con la información sobre si el mensaje fue creado o no
    return JsonResponse(json_response)

@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))