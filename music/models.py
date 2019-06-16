from django.db import models
from django.utils import timezone


class Music(models.Model):
    reference_id = models.CharField(max_length=1000, null=True)
    posted_by = models.CharField(max_length=20, null=True)
    label = models.CharField(max_length=100, null=True)
    artist = models.CharField(max_length=100, null=True)
    music_name = models.CharField(max_length=100, null=True)
    music_path = models.FileField(upload_to='music/songs/%Y/%m/%d/')
    file_ext = models.CharField(max_length=10, null=True)
    label_image = models.ImageField(upload_to='music/labels/', default='music/labels/default_label.jpg')
    artist_image = models.ImageField(upload_to='music/artists/', default='music/artists/default_artist.jpg')
    is_active = models.BooleanField(default=True)
    visits = models.IntegerField(default=0, null=True)
    release_date = models.DateField(default=timezone.now, null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
