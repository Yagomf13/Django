from django.urls import path
from .views import SingUpView, ProfileUpdate

urlpatterns = [
    path('singup/', SingUpView.as_view(), name='singup'),
    path('profile/', ProfileUpdate.as_view(), name='profile')
]
