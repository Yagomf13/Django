from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'                                         
    verbose_name = 'Portafolio'          #nombre que recibe la base de datos en el /admin
