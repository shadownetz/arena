from django.contrib.auth.models import (AbstractUser, User)
# from django.contrib.auth.base_user import BaseUserManager
from .UserManager import CustomUserManager
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class UserProfile(AbstractUser):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    username = models.CharField(_('username'), max_length=20, unique=True)
    is_staff = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=True)
    # salt = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/user_avatar.png')
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    # last_logged = models.DateTimeField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)


class Log(models.Model):
    CHOICES = (
        ('TYPE_A', 'type_A'), ('TYPE_B', 'type_B'),
    )
    user = models.CharField(max_length=100, null=True)
    category = models.CharField(choices=CHOICES, null=True, max_length=10)
    message = models.TextField(null=True)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        content = str(self.user) + '_' + str(self.timestamp.now().strftime('%Y-%m-%d_%H:%M:%S'))
        return content


class UserImage(models.Model):
    username = models.CharField(max_length=20, null=True)
    image_path = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return str(self.username)


def format_all_img_path(instance, filename):
    return 'appImages/{0}/{1}'.format(instance.ref_id, filename)


class ImageGallery(models.Model):
    ref_id = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to=format_all_img_path)
    uploaded = models.DateTimeField(default=timezone.now)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_log(sender, instance, created, **kwargs):
    if created:
        Log.objects.create(
            user=instance.username,
            category='TYPE_A',
            message='User Created Successfully',
        ).save()


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def create_user_log(sender, instance, created, **kwargs):
    if created:
        Log.objects.create(
            user=instance.username,
            category='TYPE_A',
            message='User Archived Successfully',
        ).save()
