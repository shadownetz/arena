# Generated by Django 2.2.1 on 2019-06-10 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('E', 'Error'), ('N', 'Normal')], max_length=100000, null=True)),
                ('message', models.TextField(null=True)),
                ('timestamp', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
