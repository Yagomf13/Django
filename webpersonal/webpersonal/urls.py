from django.contrib import admin
from django.urls import path
from core import views as core_views                 #para diferenciar de portfolio views
from portfolio import views as portfolio_views

from django.conf import settings   #para acceder a las variables del media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name="home"),
    path('about-me/', core_views.about, name="about"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
    path('contacto/', core_views.contacto, name="contacto")
]


if settings.DEBUG:  #si estamos en DEBUG
    from django.conf.urls.static import static  #importamos django static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #lo añadimos a la URL