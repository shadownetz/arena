# Generated by Django 2.2.1 on 2019-06-12 07:15

from django.db import migrations, models
import django.utils.timezone
import softwares.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.CharField(max_length=1000, null=True)),
                ('category', models.CharField(choices=[('A', 'android'), ('G', 'games'), ('O', 'os'), ('P', 'pc')], max_length=10, null=True)),
                ('file', models.FileField(upload_to=softwares.models.determine_software_dir_path)),
                ('file_ext', models.CharField(max_length=10, null=True)),
                ('tags', models.CharField(max_length=50, null=True)),
                ('uploaded', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]