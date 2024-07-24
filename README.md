# 🚀 Aprendiendo Django 🌟

¡Hola! 👋 Bienvenidos a mi repositorio donde estoy aprendiendo Django a través de un curso en Udemy. Aquí puedes ver todo lo que he estado creando mientras aprendo.
## 📚 Descripción

Estoy siguiendo un curso de Django en Udemy y documentando todo lo que aprendo aquí. ¡Espero que te sirva de inspiración o ayuda en tu propio camino!
## 📁 Contenido

proyectos/: Todos mis proyectos de Django.

## 🛠 Requisitos

Para ejecutar los proyectos, necesitas:

- Python
- Django
- Un entorno virtual (recomendado)

# Configuración y Ejecución de un Proyecto Django

## Requisitos Previos
Asegúrate de tener Python instalado en tu sistema.

## Pasos para Crear y Configurar el Proyecto

### 1. Crear un Entorno Virtual
Primero, crea un entorno virtual para tu proyecto:
```bash
python -m venv venv
```
2. Activar el Entorno Virtual

Activa el entorno virtual:

```bash
venv\Scripts\activate
```

3. Instalar Dependencias

Instala Django y otras dependencias necesarias:

```bash
pip install django django-ckeditor Pillow pylint pylint-django pylint-celery
```

4. Crear el Proyecto Django

Crea un nuevo proyecto Django:

```bash
django-admin startproject <Nombre-del-proyecto>
```

5. Crear una Aplicación Django

Navega al directorio del proyecto y crea una nueva aplicación:

```bash
cd <Nombre-del-proyecto>
python manage.py startapp <Nombre-de-la-app>
```

6. Ejecutar el Servidor de Desarrollo

Para asegurarte de que todo esté funcionando correctamente, ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

7. Realizar Migraciones

Crea y aplica las migraciones iniciales:

```bash
python manage.py makemigrations
python manage.py migrate
```

8. Crear un Superusuario

Crea un superusuario para acceder al administrador de Django:

```bash
python manage.py createsuperuser
```

Cambios en settings.py

Para configurar tu aplicación en Django, realiza los siguientes cambios en settings.py:
Agregar Aplicaciones a INSTALLED_APPS

```bash
INSTALLED_APPS = [
    ...,
    '<Nombre-de-la-app>',
]
```

Si estás configurando una aplicación con más configuraciones, como base de datos, agrega la configuración completa:

```bash
INSTALLED_APPS = [
        ...,
        'portfolio.apps.PortfolioConfig',
    ]
```

Ejemplo Completo de INSTALLED_APPS

python

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<Nombre-de-la-app>',
    'portfolio.apps.PortfolioConfig',
]
```


Ejecución del Proyecto

Una vez que hayas configurado todo, puedes ejecutar tu proyecto con:

```bash
python manage.py runserver
```

