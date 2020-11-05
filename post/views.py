from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView
)


from post.models import Article, Tag, Category
from post.forms import ContactForm, CategoryForm, ArticleForm


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



class Contact(FormView):
    form_class = ContactForm
    success_url = "/"
    template_name = "contact.html"

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())


class CategoryCreateView(FormView):
    form_class = CategoryForm
    success_url = "/"
    template_name = "category/create.html"

    def form_valid(self, form):
        Category.objects.create(
            name=form.data.get('name'),
            is_active=bool(form.data.get('is_active'))
        )
        return HttpResponseRedirect(self.get_success_url())


class ArticleCreateView(FormView):
    form_class = ArticleForm
    success_url = "/"
    template_name = "article/create.html"