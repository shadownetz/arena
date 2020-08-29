from django.db import models
from django.conf import settings
from index.constants import countries, states
from django.utils import timezone
# from index.functions import generate_random_value
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.shortcuts import get_object_or_404


def format_event_img_path(instance, filename):
    return 'event_center/{0}/{1}'.format(instance.ref_id, filename)


class EventCenter(models.Model):
    CHOICES = (
        ('Local', 'LOCAL'),
        ('International', 'INTERNATIONAL')
    )
    owner = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    ref_id = models.CharField(max_length=100, null=True, default='none')
    category = models.CharField(max_length=20, choices=CHOICES, null=True)
    phone = models.CharField(max_length=20, null=True)
    mail = models.EmailField(max_length=30, null=True)
    website = models.CharField(max_length=50, null=True, default='no website')
    can_book = models.BooleanField(default=False)
    address = models.TextField(max_length=100, null=True)
    availability = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    country = models.CharField(max_length=20, choices=countries())
    state = models.CharField(max_length=20, choices=states())
    image_rep = models.ImageField(upload_to=format_event_img_path)
    date_history = models.DateField(null=True)
    date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str("EventCenter")


class EventCenterReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    model = models.OneToOneField(EventCenter, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user) + ' event review'
