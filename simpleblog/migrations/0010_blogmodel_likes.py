# Generated by Django 5.1.5 on 2025-02-13 01:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0009_blogmodel_blogim'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='Likes',
            field=models.ManyToManyField(blank=True, related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
