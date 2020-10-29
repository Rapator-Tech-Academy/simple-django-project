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

    class Meta:
        verbose_name = "Blog article"
        verbose_name_plural = "Blog articles"

    def __str__(self):
        return self.title