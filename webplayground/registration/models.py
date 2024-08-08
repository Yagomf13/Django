from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver    #!Decorador
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):   #!Hacemos esto para que te borre las imagenes antiguas de los avatares
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)   #!Se te guarda despues de crearlo
def ensure_profile_exists(sender, instance, **kwargs):   #!Crea un perfil cuando se cree una cuenta automaticamente
    if kwargs.get('created', False):  #!Solo se ejecuta cuando se cree el perfil la primera vez
        Profile.objects.get_or_create(user=instance)
        print('Se acaba de crear un usuario y su perfil enlazado.')