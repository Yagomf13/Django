from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')            #!Muestra los valores en el /admin
    ordering = ('author', 'published')                                            #!Ordena los valores en el /admin si quires poner solo uno asi ordering = ('author',) si no se queja
    search_fields = ('title', 'content', 'author__username', 'categories__name')  #!Busca por titulo si quieres buscar por username se pone author__username y por categorias por categories__name
    date_hierarchy = 'published'                                                  #!Forma mas comoda de buscar por fecha
    list_filter = ('author__username', 'categories__name')                        #!Añade un filtro para buscar más rápido

    def post_categories(self, obj):                                               #!Se usa para mostrar las categorias ya que de por si no puede porque no son del modelo
        return ", ".join([category.name for category in obj.categories.all().order_by('name')])
    post_categories.short_description = "Categorias"                              #!Asigna el nombre de categorias añ filtro


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)