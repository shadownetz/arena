# Generated by Django 2.2.1 on 2019-06-10 14:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20190610_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(null=True, on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
