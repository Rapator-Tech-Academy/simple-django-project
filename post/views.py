from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)


from post.models import Article, Tag


class HomePage(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "index.html"

    def get_queryset(self):
        return Article.objects.filter(is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['tags'] = Tag.objects.all()
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = "detail.html"
    context_object_name = "article"