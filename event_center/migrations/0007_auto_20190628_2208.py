# Generated by Django 2.2.1 on 2019-06-28 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_center', '0006_auto_20190628_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcenter',
            name='ref_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]