# Generated by Django 3.2.7 on 2022-06-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_auto_20220608_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.BooleanField(default=False),
        ),
    ]
