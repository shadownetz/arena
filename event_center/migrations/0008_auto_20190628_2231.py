# Generated by Django 2.2.1 on 2019-06-28 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_center', '0007_auto_20190628_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcenter',
            name='ref_id',
            field=models.CharField(default='none', max_length=10, null=True),
        ),
    ]
