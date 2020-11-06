from django import forms

from post.models import Article


class ContactForm(forms.Form):
    choices = (
        ("t1", ("test 1")),
        ("t2", ("test 2")),
        ("t3", ("test 3")),
    )
    name = forms.CharField(
        label="Your name",
        max_length=100
    )
    surname = forms.CharField(
        label="Your surname",
        max_length=100
    )
    test = forms.ChoiceField(
        choices=choices
    )
    date = forms.DateTimeField()


class CategoryForm(forms.Form):
    name = forms.CharField(label="Category Name", help_text="Example: News", max_length=30)
    is_active = forms.BooleanField(required=False, initial=True)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label="Title of the article", max_length=100)
    class Meta:
        model = Article
        fields = ['title', 'body', 'featured_image', 'category', 'tags', 'slug']