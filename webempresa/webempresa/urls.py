from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Paths del core
    # importamos de core.urls los enlaces
    path('', include('core.urls')),

    # Paths del services
    path('services/', include('services.urls')),

    # Paths del blog
    path('blog/', include('blog.urls')),

    # Paths del sample
    path('page/', include('pages.urls')),

    # Paths del contact
    path('contact/', include('contact.urls')),

    # Paths del admin
    path('admin/', admin.site.urls),
]
