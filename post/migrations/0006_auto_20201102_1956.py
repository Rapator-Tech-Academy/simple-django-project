# Generated by Django 3.1.2 on 2020-11-02 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='active_duration',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='article',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='post.category'),
        ),
    ]
