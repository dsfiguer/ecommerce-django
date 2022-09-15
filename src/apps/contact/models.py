from django.db import models
from django.utils import timezone

from apps.website.models import Website


class ContactInfo(models.Model):
    def __str__(self):
        return f'{self.id}-{self.email}-{self.created_at}'

    site = models.ForeignKey(Website, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    note = models.TextField()
    responded = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now, editable=False)
