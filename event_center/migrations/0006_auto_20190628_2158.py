# Generated by Django 2.2.1 on 2019-06-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_center', '0005_auto_20190628_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcenter',
            name='ref_id',
            field=models.CharField(default='adbddc560ee0c4dd3b00', max_length=10, null=True),
        ),
    ]