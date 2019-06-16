# Generated by Django 2.2.1 on 2019-06-11 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_by', models.CharField(max_length=25, null=True)),
                ('category', models.CharField(choices=[('G', 'gist'), ('T', 'tech'), ('N', 'news')], max_length=10, null=True)),
                ('heading', models.CharField(max_length=200, null=True)),
                ('content', models.TextField(max_length=100000, null=True)),
                ('post_image', models.ImageField(upload_to='images/')),
                ('tags', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]