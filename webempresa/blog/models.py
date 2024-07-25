from django.db import models
from django.utils.timezone import now            #! Importa zona horaria donde esta el proyecto para ponerlo automaticamente en el published
from django.contrib.auth.models import User  #! Importa modelo de usuarios para el autor

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Caregorias'
        ordering = ['-created']

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de Publicación', default=now)             #! Se usa timezone
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)           #! Se usa User
    categories = models.ManyToManyField(Category,verbose_name='Categories', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title