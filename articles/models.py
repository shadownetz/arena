from django.db import models


class Article(models.Model):
    reference_id = models.CharField(max_length=1000, null=True)
    author = models.CharField(max_length=50, null=True)
    heading = models.CharField(max_length=100, null=True)
    content = models.TextField(max_length=10000, null=True)
    image = models.ImageField(upload_to='articles/images', default='articles/images/%Y/%m')
    file = models.FileField(upload_to='articles/files', default='articles/files/%Y/%m')
    visits = models.IntegerField(default=0, null=True)
    tags = models.CharField(max_length=50, null=True)
