# Generated by Django 2.2.1 on 2019-06-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='post_image',
            field=models.ImageField(default='images/default_info.jpg', upload_to='images/'),
        ),
    ]
