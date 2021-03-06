# Generated by Django 3.1.2 on 2020-11-19 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201119_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'User Device',
                'verbose_name_plural': 'User Devices',
            },
        ),
    ]
