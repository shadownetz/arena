# Generated by Django 2.2.1 on 2019-06-13 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20190613_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]
