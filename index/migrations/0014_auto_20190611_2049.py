# Generated by Django 2.2.1 on 2019-06-11 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20190610_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('image_path', models.ImageField(upload_to='avatars/')),
            ],
        ),
        migrations.AlterField(
            model_name='log',
            name='category',
            field=models.CharField(choices=[('A', 'type_A'), ('B', 'type_B')], max_length=10, null=True),
        ),
    ]
