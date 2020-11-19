from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model, login as auth_login, logout
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,

    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetDoneView
)

from django.views.generic.edit import FormView

from users.forms import (
    CustomAuthenticationForm,
    CustomPasswordChangeForm
)

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
        valid_user = get_object_or_404(
            User.objects.all(),
            username=username
        )
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
        return super().form_valid(form)
        



class CustomLogoutView(LogoutView):

    def get_next_page(self):
        return reverse('login')


#class CustomPasswordChangeView(PasswordChangeView):
#    template_name = "users/password/change.html"
#    success_url = reverse_lazy("login")


class CustomPasswordChangeView(FormView):
    form_class = CustomPasswordChangeForm
    template_name = "users/password/change.html"
    success_url = reverse_lazy("login")

    def check_old_password(self, form):
        old_pass = form.cleaned_data.get('old_password')
        user = self.request.user
        return user.check_password(old_pass)

    def form_valid(self, form):
        is_old_true = self.check_old_password(form)
        if is_old_true:
            new_password = form.cleaned_data.get('new_password')
            self.request.user.set_password(new_password)
            self.request.user.save()
        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    template_name = "users/password/reset.html"
    success_url = reverse_lazy("login")
    email_template_name = "emails/password_reset_email.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password/reset-confirm.html"
    success_url = reverse_lazy("password-reset-complete")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password/reset-complete.html"
    success_url = reverse_lazy("login")