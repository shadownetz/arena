from django.db import models
from django.utils import timezone


class Info(models.Model):
    CHOICES = (
        ('G', 'gist'),
        ('T', 'tech'),
        ('N', 'news'),
    )
    reference_id = models.CharField(max_length=1000, null=True)
    post_by = models.CharField(max_length=25, null=True)
    category = models.CharField(max_length=10, choices=CHOICES, null=True)
    heading = models.CharField(max_length=200, null=True)
    content = models.TextField(max_length=100000, null=True)
    post_image = models.ImageField(upload_to='info/images/', default='info/images/default_info.jpg')
    tags = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    visits = models.IntegerField(default=0, null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
