from django.db import models
from index.constants import countries, states
from django.utils import timezone
from django.conf import settings


def format_food_drink_img_path(instance, filename):
    return 'food_drink/{0}/{1}'.format(instance.ref_id, filename)


class FoodDrink(models.Model):
    CHOICES = (
        ('Local', 'LOCAL'),
        ('International', 'INTERNATIONAL')
    )
    category = models.CharField(max_length=20, choices=CHOICES, null=True)
    ref_id = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=20, null=True)
    ingredients = models.TextField(max_length=500, null=True)
    rating = models.IntegerField(default=0)
    assoc_country = models.CharField(max_length=20, choices=countries())
    assoc_states = models.CharField(max_length=20, choices=states())
    image_rep = models.ImageField(upload_to=format_food_drink_img_path)
    date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str("Food&Drink")


class FoodDrinkReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    model = models.OneToOneField(FoodDrink, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
