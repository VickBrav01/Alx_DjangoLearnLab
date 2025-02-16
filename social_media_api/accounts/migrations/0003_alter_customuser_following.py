# Generated by Django 5.1.3 on 2024-12-13 12:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_following_alter_customuser_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(related_name='user_following', to=settings.AUTH_USER_MODEL),
        ),
    ]
