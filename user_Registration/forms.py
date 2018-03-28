from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required')
    mobile = forms.CharField(max_length=15, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'mobile')