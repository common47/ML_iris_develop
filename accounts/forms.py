from django import forms
from django.contrib.auth.models import User
from .models import PredUser

from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': None,
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = PredUser
        fields = '__all__'

