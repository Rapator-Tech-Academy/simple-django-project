from django.urls import path

from . import views


urlpatterns = [
    path("", views.UsersHome.as_view(), name="users-home"),
    path("list/", views.UsersList.as_view(), name="users-list"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
]
