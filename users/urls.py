from users.views import CustomPasswordResetView
from django.urls import path

from . import views


urlpatterns = [
    path("", views.UsersHome.as_view(), name="users-home"),
    path("list/", views.UsersList.as_view(), name="users-list"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),

    path("password/change/", views.CustomPasswordChangeView.as_view(), name="password-change"),

    path("password/reset/", views.CustomPasswordResetView.as_view(), name="password-reset"),
    path("password/reset/confirm/<uidb64>/<token>", views.CustomPasswordResetConfirmView.as_view(), name="password-confirm"),
    path("password/reset/complete/", views.CustomPasswordResetCompleteView.as_view(), name="password-reset-complete"),
]
