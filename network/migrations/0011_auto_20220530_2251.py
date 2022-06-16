# Generated by Django 3.2.7 on 2022-05-30 22:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_auto_20220530_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follows',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='_network_user_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
