from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        # Specifies the model to be used for the form
        model = User
        # Specifies the fields to be included in the form
        fields = ['username', 'password1', 'password2']
