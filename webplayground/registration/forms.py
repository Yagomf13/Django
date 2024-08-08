from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

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
    

class ProfileForm(forms.ModelForm):         #! Mostrar el formulario clean
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Biografía'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Enlace'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como máximo y debe ser valido')  #! Hacer que el email sea único

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):    #! Comprueba si el email esta siendo utilizado
        email = self.cleaned_data['email']
        if 'email' in self.cleaned_data.get('email'):    #! Lista que almacena todos los campos que se han cambiado en el formulario    El email tiene que haber cambiado
            if User.objects.filter(email=email).exists():  #! Si esta creado realiza error
                raise forms.ValidationError('El email ya está registrado prueba con otro.')
        return email
