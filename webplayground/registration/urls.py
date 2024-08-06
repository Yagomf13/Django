from django.urls import path
from .views import SingUpView

urlpatterns = [
    path('singup/', SingUpView.as_view(), name='singup'),
]
