from distutils.command.upload import upload
import random
import string
from unicodedata import decimal

from django.utils.text import slugify
from django.db import models
from django.utils import timezone

from apps.website.models import Website


class Category(models.Model):
    def __str__(self):
        return self.category

    category = models.CharField(max_length=50)


class Product(models.Model):
    def _set_sku():
        random_nums = str(random.randint(1000, 9999))
        random_alph = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
        return random_alph + random_nums

    def _set_slug(self):
        self.slug = slugify(self.name)

    def _set_profit(self):
        self.profit = self.price - self.wholesaler_price
    
    def _2_dec_places(self):
        self.profit = round(self.profit, 2)
    
    def save(self, *args, **kwargs):
        self._set_slug()
        self._set_profit()
        self._2_dec_places()
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
    categories = models.ManyToManyField(Category)

    sku = models.CharField(max_length=8, default=_set_sku(), unique=True, primary_key=True, editable=False)
    slug = models.SlugField(max_length=25, unique=True, blank=True, editable=False)
    profit = models.FloatField(default=0.0, editable=False, )
    created_at = models.DateField(default=timezone.now, editable=False)

    is_available = models.BooleanField(default=True)


class ProductPictures(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pics")
    picture = models.ImageField(upload_to="product/")
    thumbnail = models.BooleanField(default=False)


class ProductVariant(models.Model):
    def __str__(self):
        return self.title

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variant")
    title = models.CharField(max_length=50)
