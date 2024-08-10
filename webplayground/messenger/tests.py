#! Si se quiere ejecutar unicamente un test se pone python manage.py test messenger .tests.ThreadTestCase

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message

# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        # Se crean dos usuarios para usarlos en las pruebas
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')
        self.user3 = User.objects.create_user('user3', None, 'test1234')

        # Se crea un objeto Thread (hilo) vacío para usarse en las pruebas
        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self):
        # Agrega los dos usuarios creados al hilo
        self.thread.users.add(self.user1, self.user2)

        # Verifica que el número de usuarios en el hilo es 2
        self.assertEqual(len(self.thread.users.all()), 2)

    def test_filter_thread_by_user(self):
        # Agrega los dos usuarios al hilo como en la prueba anterior
        self.thread.users.add(self.user1, self.user2)

        # Filtra los hilos que contienen tanto a user1 como a user2
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)

        # Verifica que el primer hilo en la lista filtrada (threads[0]) es el mismo que el hilo creado en setUp (self.thread)
        self.assertEqual(self.thread, threads[0])

    def test_filter_non_existent_threads(self):
        # Filtra los hilos que contienen tanto a user1 como a user2
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)

        # Verifica que no se encontró ningún hilo en la lista filtrada (la longitud de `threads` es 0)
        self.assertEqual(len(threads), 0)

    def test_add_messages_to_thread(self):
        # Agrega los dos usuarios creados al hilo
        self.thread.users.add(self.user1, self.user2)

        # Crea dos mensajes, uno de cada usuario, con contenido diferente
        message1 = Message.objects.create(user=self.user1, content='Muy buenas')
        message2 = Message.objects.create(user=self.user2, content='Hola')

        # Añade los dos mensajes creados al hilo
        self.thread.messages.add(message1, message2)

        # Verifica que el número de mensajes en el hilo es 2
        self.assertEqual(len(self.thread.messages.all()), 2)

        # Itera sobre todos los mensajes en el hilo e imprime el usuario y el contenido de cada mensaje
        for message in self.thread.messages.all():
            print("({}): {}".format(message.user, message.content))
    
    def test_add_messages_from_user_not_in_thread(self):
        # Agrega los dos usuarios creados al hilo
        self.thread.users.add(self.user1, self.user2)
        
        # Crea dos mensajes, uno de cada usuario, con contenido diferente
        message1 = Message.objects.create(user=self.user1, content='Muy buenas')
        message2 = Message.objects.create(user=self.user2, content='Hola')
        message3 = Message.objects.create(user=self.user3, content='Soy un espia')

        # Añade los dos mensajes creados al hilo
        self.thread.messages.add(message1, message2, message3)

        # Verifica que el número de mensajes en el hilo es 2
        self.assertEqual(len(self.thread.messages.all()), 2)

    def test_find_thread_with_custom_manager(self):
        # Agrega los dos usuarios creados al hilo
        self.thread.users.add(self.user1, self.user2)

        # Usa el método 'find' del ThreadManager para encontrar el hilo que contiene tanto a user1 como a user2
        thread = Thread.objects.find(self.user1, self.user2)

        # Verifica que el hilo encontrado es el mismo que el hilo creado en setUp
        self.assertEqual(self.thread, thread)

    def test_find_thread_with_custom_manager(self):
        # Agrega los dos usuarios creados al hilo
        self.thread.users.add(self.user1, self.user2)

        # Usa el método 'find' del ThreadManager para encontrar el hilo que contiene tanto a user1 como a user2
        thread = Thread.objects.find_or_create(self.user1, self.user2)

        # Verifica que el hilo encontrado es el mismo que el hilo creado en setUp
        self.assertEqual(self.thread, thread)

        # Usa el método 'find' del ThreadManager para encontrar el hilo que contiene tanto a user1 como a user2
        thread = Thread.objects.find_or_create(self.user1, self.user3)

        # Verifica que el hilo encontrado es el mismo que el hilo creado en setUp
        self.assertIsNotNone(self.thread, thread)
