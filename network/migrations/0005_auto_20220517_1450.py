# Generated by Django 3.2.7 on 2022-05-17 14:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_like_likers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='link',
        ),
        migrations.AlterField(
            model_name='like',
            name='haters',
            field=models.ManyToManyField(blank=True, null=True, related_name='haters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='likers',
            field=models.ManyToManyField(blank=True, null=True, related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
    ]
