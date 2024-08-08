from django.urls import path
from .views import SingUpView, ProfileUpdate, EmailUpdate

urlpatterns = [
    path('singup/', SingUpView.as_view(), name='singup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', EmailUpdate.as_view(), name='profile_email')
]
