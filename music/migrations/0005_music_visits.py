# Generated by Django 2.2.1 on 2019-06-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_music_reference_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='visits',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
