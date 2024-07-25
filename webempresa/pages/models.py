from django.db import models
from ckeditor.fields import RichTextField    #!Importamos el editor de texto

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')  #!Lo sustitumos por el models...
    order = models.SmallIntegerField(verbose_name='Orden', default=0)  #!Ordenar en el orden que quiera el usuario
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')


    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title