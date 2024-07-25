from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre Clave', max_length=100, unique=True)
    name = models.CharField(max_length=200, verbose_name='Red social')
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')


    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name']

    def __str__(self):
        return self.name