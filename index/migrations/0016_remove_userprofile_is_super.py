# Generated by Django 2.2.1 on 2019-06-13 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_auto_20190612_0726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_super',
        ),
    ]