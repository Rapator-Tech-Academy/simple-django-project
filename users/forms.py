from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)



class CustomPasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, max_length=30, min_length=5)
    new_password = forms.CharField(widget=forms.PasswordInput, max_length=30, min_length=5)
    new_password2 = forms.CharField(widget=forms.PasswordInput, max_length=30, min_length=5)

    def clean(self):
        data = super().clean()
        if data.get('new_password') == data.get('old_password'):
            self.add_error("new_password", "Old password is not accepted")
        
        if data.get('new_password') != data.get('new_password2'):
            self.add_error("new_password", "Passwords didnt match")
