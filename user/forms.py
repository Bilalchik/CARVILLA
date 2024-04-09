from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import MyUser


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('phone_number', 'first_name', 'email', 'password1', 'password2')


class UserLoginForm(forms.Form):
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

