from django.db import models
from index.models import UserProfile
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True)
    nick_name = models.CharField(max_length=20, null=True)
    about = models.TextField(max_length=300, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()


class Archive(models.Model):
    username = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateTimeField(null=True)
    date_deleted = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return str(self.username)


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL, dispatch_uid='user_delete_signal')
def move_profile_to_archive(sender, instance, using, **kwargs):
    Archive.objects.create(
        username=instance.username,
        email=instance.email,
        date_created=instance.date_created
    ).save()


class Message(models.Model):
    CHOICES = (
        ('D', 'download'),
        ('V', 'visit'),
        ('A2U', 'admin2user')
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50, null=True)
    content = models.TextField(max_length=1000, null=True)
    category = models.CharField(choices=CHOICES, max_length=10, null=True)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now, null=True)

