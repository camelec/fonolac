from django import forms
from .models import User
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""

    password1 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Repetir Contraseña '
            }
        )
    )

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'La contraseña no coincide')

class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'username',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'username'
            }
        )
    )
    password = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username = username, password = password):
            raise forms.ValidationError('Los datos de ususrio no son correctos')
        
        return self.cleaned_data

class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña actual'
            }
        )
    )
    password2 = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Contraseña nueva'
            }
        )
    )