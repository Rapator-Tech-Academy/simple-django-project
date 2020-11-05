from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomePage.as_view(), name="home-page"),
    path("article/<slug>/", views.ArticleDetail.as_view(), name="article-detail"),
    path("contact/", views.Contact.as_view(), name="contact-page"),

    path("create-category/", views.CategoryCreateView.as_view(), name="category-create"),

    path("create-article/", views.ArticleCreateView.as_view(), name="article-create"),
]
