from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth import get_user_model


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