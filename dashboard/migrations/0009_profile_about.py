# Generated by Django 2.2.1 on 2019-06-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20190612_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
