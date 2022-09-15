from django.db import models
from django.utils import timezone


class Website(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=25, unique=True)
    url = models.URLField()
    logo = models.ImageField(upload_to="site/logo/")
    favicon = models.ImageField(upload_to="site/favicon/")

    created_at = models.DateField(default=timezone.now, editable=False)

    is_available = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
