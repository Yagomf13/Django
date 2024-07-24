from django.contrib import admin
from .models import Project                 #importamos el modelo

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)  #registramos el modelo en la base de datos