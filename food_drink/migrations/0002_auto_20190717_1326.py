# Generated by Django 2.2.1 on 2019-07-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_drink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddrink',
            name='assoc_country',
            field=models.CharField(choices=[('Nigeria', 'NIGERIA')], max_length=20),
        ),
        migrations.AlterField(
            model_name='fooddrink',
            name='assoc_states',
            field=models.CharField(choices=[('Abia', 'ABIA'), ('Enugu', 'ENUGU'), ('Lagos', 'LAGOS')], max_length=20),
        ),
        migrations.AlterField(
            model_name='fooddrink',
            name='category',
            field=models.CharField(choices=[('Local', 'LOCAL'), ('International', 'INTERNATIONAL')], max_length=20, null=True),
        ),
    ]
