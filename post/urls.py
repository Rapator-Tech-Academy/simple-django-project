from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomePage.as_view(), name="home-page"),
    path("article/<slug>/", views.ArticleDetail.as_view(), name="article-detail"),
]
