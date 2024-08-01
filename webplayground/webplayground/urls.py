from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),   #añadir el nombre del pattern
    path('admin/', admin.site.urls),
]
