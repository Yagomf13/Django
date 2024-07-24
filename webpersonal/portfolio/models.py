from django.db import models

class Project(models.Model):                                                                  #creamos el modelo
    title = models.CharField(max_length=200, verbose_name='Titulo')                           #title
    description = models.TextField(verbose_name='Descripción')                                #description
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')                    #image y las guarda en la carpeta projects
    url = models.URLField(verbose_name="url", blank=True, null=True)                          #url como se creo despues debe de poder tener valores vacios
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')       #cuando se creo
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')       #cuando se modifico por ultima vez


    class Meta:
        verbose_name = 'Proyecto'                        #nombre singula
        verbose_name_plural = 'Proyectos'                #nombre plural
        ordering = ['-created']                          #como se ordena

    def __str__(self):
        return self.title                                #mostrar el titulo en el admin