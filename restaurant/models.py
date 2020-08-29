from django.db import models
from django.utils import timezone
from index.constants import countries, states
from index.models import UserProfile
# from django.dispatch import receiver
# from django.db.models.signals import pre_save
from django.conf import settings


def format_restaurant_img_path(instance, filename):
    return 'restaurants/{0}/{1}'.format(instance.ref_id, filename)


class Restaurant(models.Model):
    CHOICES = (
        ('Local', 'LOCAL'),
        ('International', 'INTERNATIONAL')
    )
    owner = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    ref_id = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CHOICES, null=True)
    phone = models.CharField(max_length=20, null=True)
    mail = models.EmailField(max_length=30, null=True)
    website = models.CharField(max_length=50, null=True)
    has_extras = models.BooleanField(default=False)
    can_book = models.BooleanField(default=False)
    can_place_order = models.BooleanField(default=False)
    can_make_home_delivery = models.BooleanField(default=False)
    address = models.TextField(max_length=100, null=True)
    country = models.CharField(max_length=20, choices=countries())
    state = models.CharField(max_length=20, choices=states())
    rating = models.IntegerField(default=0)
    open_time = models.TimeField(null=True)
    close_time = models.TimeField(null=True)
    image_rep = models.ImageField(upload_to=format_restaurant_img_path)
    date_history = models.DateField(null=True)
    date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str("Restaurant")


class RestaurantReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    model = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
# @receiver(pre_save, sender=Restaurant)
# def assign_reference_id(sender, instance, **kwargs):
#         tmp = instance.owner.username[:3] + instance.name[:3] + str(instance.id)
#         instance.ref_id = tmp
#         # instance.save()
