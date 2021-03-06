from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name="Title of the article"
    )
    body = models.TextField(
        verbose_name="Body of the article"
    )
    featured_image = models.ImageField()
    category = models.ForeignKey(
        "post.Category",
        on_delete=models.SET_NULL,
        related_name="articles",
        null=True
    )
    tags = models.ManyToManyField(
        "post.Tag",
        related_name="articles"
    )
    view_count = models.PositiveIntegerField(default=0)
    slug = models.SlugField(null=True, unique=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = "Blog article"
        verbose_name_plural = "Blog articles"

    def __str__(self):
        return self.title