# Generated by Django 2.2.1 on 2019-06-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_remove_userprofile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatars/user_avatar.png', upload_to='avatars/'),
        ),
    ]
