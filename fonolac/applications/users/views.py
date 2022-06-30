from django.shortcuts import render
from django.views.generic import (
    CreateView
)
from django.views.generic.edit import (
    FormView
)

# Create your views here.

from .forms import UserRegisterForm
from .models import User

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
        )
        #
        return super(UserRegisterView, self).form_valid(form)