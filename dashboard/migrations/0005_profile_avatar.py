# Generated by Django 2.2.1 on 2019-06-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190610_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='user_avatar.jpg', upload_to='avatars/'),
        ),
    ]
