# Generated by Django 2.2.1 on 2019-06-24 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_country_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(choices=[('ABA', 'Abia'), ('EN', 'Enugu'), ('LG', 'Lagos')], max_length=50),
        ),
    ]
