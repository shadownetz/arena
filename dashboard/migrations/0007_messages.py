# Generated by Django 2.2.1 on 2019-06-12 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0006_auto_20190611_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50, null=True)),
                ('content', models.TextField(max_length=1000, null=True)),
                ('category', models.CharField(choices=[('D', 'download'), ('V', 'visit'), ('A2U', 'admin2user')], max_length=10, null=True)),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
