from django.contrib import admin
from django.urls import path, include
from django.conf import settings

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

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Custom titles for admin
admin.site.site_header = 'La Caffetiera'  #Cambiar el titulo del admin
admin.site.index_title = 'Panel de Administrados'
admin.site.site_title = 'La Caffetiera'

