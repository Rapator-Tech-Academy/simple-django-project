from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)