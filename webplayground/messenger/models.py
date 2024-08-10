from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class ThreadManager(models.Manager):
    def find(self, user1, user2):
        # Filtra los hilos que contienen tanto a user1 como a user2
        queryset = self.filter(users=user1).filter(users=user2)

        # Si existe al menos un hilo que cumpla con los criterios, retorna el primero
        if len(queryset) > 0:
            return queryset[0]
        
        # Si no se encontró ningún hilo, retorna None
        return None
    
    def find_or_create(self, user1, user2):
        # Intenta encontrar un hilo que contenga tanto a user1 como a user2 usando el método 'find'
        thread = self.find(user1, user2)

        # Si no se encontró ningún hilo (thread es None)
        if thread is None:
            # Crea un nuevo hilo
            thread = Thread.objects.create()

            # Añade a user1 y user2 al nuevo hilo
            thread.users.add(user1, user2)

        # Retorna el hilo encontrado o el recién creado
        return thread



class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    updated = models.DateTimeField(auto_now=True)

    objects = ThreadManager()

    class Meta:
        ordering = ['-updated']

def messages_changed(sender, **kwargs):
    # Extrae la instancia de Thread, la acción realizada y el conjunto de pks de los mensajes involucrados
    instance = kwargs.pop('instance', None)
    action = kwargs.pop('action', None)
    pk_set = kwargs.pop('pk_set', None)
    
    # Imprime la instancia del Thread, la acción realizada y los pks de los mensajes involucrados
    print(instance, action, pk_set)

    # Conjunto para almacenar los pks de mensajes que no deberían ser añadidos al hilo
    false_pk_set = set()

    # Si la acción es 'pre_add' (antes de añadir mensajes al hilo)
    if action == 'pre_add':
        # Itera sobre los pks de los mensajes que se van a añadir
        for msg_pk in pk_set:
            # Obtiene el mensaje por su pk
            msg = Message.objects.get(pk=msg_pk)
            # Verifica si el usuario que envió el mensaje no es parte del hilo
            if msg.user not in instance.users.all():
                # Si el usuario no es parte del hilo, imprime un mensaje de advertencia
                print("Ups, ({}) no forma parte del hilo".format(msg.user))
                # Añade el pk del mensaje al conjunto false_pk_set para evitar que se añada al hilo
                false_pk_set.add(msg_pk)

    # Elimina de pk_set los mensajes que están en false_pk_set para que no se añadan al hilo
    pk_set.difference_update(false_pk_set)

    # Forzarla actualización haciendo un save
    instance.save()

# Conecta la señal m2m_changed a la función messages_changed para monitorear cambios en la relación ManyToMany
m2m_changed.connect(messages_changed, sender=Thread.messages.through)
