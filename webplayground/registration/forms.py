from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como máximo y debe ser valido')  #! Hacer que el email sea único

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):    #! Comprueba si el email esta siendo utilizado
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():  #! Si esta creado realiza error
            raise forms.ValidationError('El email ya está registrado prueba con otro.')
        return email