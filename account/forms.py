from django import forms
from django.contrib.auth.forms import AuthenticationForm

from account.models import User


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-mail'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ['email', 'password']
