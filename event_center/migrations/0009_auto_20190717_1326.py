# Generated by Django 2.2.1 on 2019-07-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_center', '0008_auto_20190628_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcenter',
            name='category',
            field=models.CharField(choices=[('Local', 'LOCAL'), ('International', 'INTERNATIONAL')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eventcenter',
            name='country',
            field=models.CharField(choices=[('Nigeria', 'NIGERIA')], max_length=20),
        ),
        migrations.AlterField(
            model_name='eventcenter',
            name='ref_id',
            field=models.CharField(default='none', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='eventcenter',
            name='state',
            field=models.CharField(choices=[('Abia', 'ABIA'), ('Enugu', 'ENUGU'), ('Lagos', 'LAGOS')], max_length=20),
        ),
    ]
