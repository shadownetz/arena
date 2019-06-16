from django.db import models
from django.utils import timezone


def determine_software_dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<choice>/<filename>
    return 'softwares/{0}/{1}/'.format(instance.category, filename)


class Software(models.Model):
    CHOICES = (
        ('Android', 'android'),
        ('Games', 'games'),
        ('OS', 'os'),
        ('PC', 'pc')
    )
    reference_id = models.CharField(max_length=1000, null=True)
    version = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=1.00)
    category = models.CharField(max_length=10, choices=CHOICES, null=True)
    file = models.FileField(upload_to=determine_software_dir_path)
    file_ext = models.CharField(max_length=10, null=True)
    visits = models.IntegerField(default=0, null=True)
    tags = models.CharField(max_length=50, null=True)
    uploaded = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return str(self.reference_id)
