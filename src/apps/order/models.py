import random
import string

from django.db import models
from django.utils import timezone

from apps.website.models import Website
from apps.cart.models import Cart, CartItem


class Order(models.Model):
    def _set_full_address(self):
        self.full_address = f'''{self.first_name} {self.last_name}
        {self.address_1} {self.address_2 if self.address_2 else ""}
        {self.city}, {self.state} {self.zipcode}'''

    def _set_order_number():
        random_nums = str(random.randint(10001, 99999))
        random_alph = ''.join(random.choice(string.ascii_uppercase) for i in range(5))
        return random_alph + random_nums
    
    def _track_quantity_sold(self):
        cartitems = CartItem.objects.filter(cart=self.cart)

        for item in cartitems:
            product = item.product
            product.quantity -= 1
            product.sold += 1
            product.save()
    
    def save(self, *args, **kwargs):
        self._track_quantity_sold()
        self._set_full_address()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    site = models.ForeignKey(Website, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

    referral = models.BooleanField(default=False)
    referral_source = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    valid_address = models.BooleanField(default=False)
    tracking = models.CharField(max_length=100, blank=True, null=True)
    shipped = models.BooleanField(default=False)
    refund = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    full_address = models.TextField(blank=True, null=True, editable=False)
    placed = models.DateTimeField(default=timezone.now, editable=False)
    order_number = models.CharField(
        max_length=10,
        default=_set_order_number(),
        unique=True,
        primary_key=True,
        editable=False
    )

