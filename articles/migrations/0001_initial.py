# Generated by Django 2.2.1 on 2019-06-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, null=True)),
                ('heading', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(max_length=10000, null=True)),
                ('image', models.ImageField(default='articles/images/%Y/%m', upload_to='articles/images')),
                ('file', models.FileField(default='articles/files/%Y/%m', upload_to='articles/files')),
                ('tags', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]