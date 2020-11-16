from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse

from django.contrib.auth import get_user_model, login as auth_login, logout
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from django.views.generic.edit import FormView

from users.forms import CustomAuthenticationForm


User = get_user_model()


class UsersHome(TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = self.request.user.username
        return context


class UsersList(TemplateView):
    template_name = "users/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['users'] = User.objects.all()
        return context


#class CustomLoginView(LoginView):
#    template_name = "users/login.html"
#
#    def get_success_url(self):
#        return reverse('home-page')


class CustomLoginView(FormView):
    form_class = CustomAuthenticationForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse('home-page')
    
    def get_user(self, form):
        username = form.cleaned_data.get('username')
        valid_user = User.objects.filter(username=username).first()
        return valid_user

    def check_password(self, user, form):
        password = form.cleaned_data.get('password')
        return user.check_password(password)

    def form_valid(self, form):
        user = self.get_user(form=form)
        if user:
            is_valid_password = self.check_password(user=user, form=form)
            if is_valid_password:
                auth_login(self.request, user)
                return super().form_valid(form)
        



class CustomLogoutView(LogoutView):

    def get_next_page(self):
        return reverse('login')