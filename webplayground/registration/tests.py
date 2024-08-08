from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

#TODO: Con esto se crean pruebas para testear si van bien las cosas

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1234')  #!Genera un usuario de prueba

    def test_profile_create(self):
        exists = Profile.objects.filter(user__username='test').exists()   #!Comprueba si existe
        self.assertEqual(exists, True)