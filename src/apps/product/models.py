from distutils.command.upload import upload
import random
import string

from django.utils.text import slugify
from django.db import models
from django.utils import timezone

from apps.website.models import Website


class Product(models.Model):
    def _set_sku():
        random_nums = str(random.randint(1000, 9999))
        random_alph = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
        return random_alph + random_nums

    def _set_slug(self):
        self.slug = slugify(self.name)

    def _set_profit(self):
        self.profit = self.price - self.wholesaler_price
    
    def save(self, *args, **kwargs):
        self._set_slug()
        self._set_profit()
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    name = models.CharField(max_length=25, unique=True)
    quantity = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    price = models.FloatField()
    wholesale_url = models.URLField()
    wholesaler_price = models.FloatField()
    description = models.TextField(null=True, blank=True)

    site = models.ForeignKey(Website, on_delete=models.CASCADE)

    sku = models.CharField(max_length=8, default=_set_sku(), unique=True, primary_key=True, editable=False)
    slug = models.SlugField(max_length=25, unique=True, blank=True, editable=False)
    profit = models.FloatField(default=0.0, editable=False)
    created_at = models.DateField(default=timezone.now, editable=False)

    is_available = models.BooleanField(default=True)


class ProductPictures(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="product/")
    thumbnail = models.BooleanField(default=False)

