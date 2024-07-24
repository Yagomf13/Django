from django.contrib import admin
from .models import Service   #! importante

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)  #! importante