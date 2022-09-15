from itertools import product
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from apps.website.models import Website
from apps.product.models import Product


class Discount(models.Model):
    def _validate_discount(percentage):
        if percentage > 1 or percentage < 0:
            raise ValidationError(
                "Must be: 0 < DISCOUNT <= 1"
            )

    def __str__(self):
        return self.code

    code = models.CharField(max_length=20)
    percentage = models.FloatField(validators=[_validate_discount])

    site = models.ForeignKey(Website, on_delete=models.CASCADE)


class Cart(models.Model):
    def _set_discounted_amount(self):
        if not self.discount:
            self.discounted_amount = None

        if self.discount and not self.discounted_amount:
            self.discounted_amount = self.total_price * self.discount.percentage
    
    def _set_price_profit(self):
        profit = 0.0
        price = 0.0
        cart_items = CartItem.objects.filter(cart=self)
        for item in cart_items:
            profit = profit + item.product.profit
            price = price + item.product.price
        
        if self.discounted_amount:
            profit = profit - self.discounted_amount
            price = price - self.discounted_amount
        
        self.total_profit = profit
        self.total_price = price
    
    def save(self, *args, **kwargs):
        self._set_discounted_amount()
        self._set_price_profit()
        super(Cart, self).save(*args, **kwargs)

    def __str__(self):
        return self.created_at.__str__()

    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)

    total_price = models.FloatField(blank=True, null=True, editable=False)
    discounted_amount = models.FloatField(blank=True, null=True, editable=False)
    total_profit = models.FloatField(blank=True, null=True, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)


class CartItem(models.Model):
    def _validate_cartitem(self):
        if not self.pk:
            cartitems = len(CartItem.objects.filter(product=self.product, cart=self.cart))
            if self.product.quantity - cartitems < 0:
                return False

        return True

    def _set_price(self):
        self.price = self.product.price
    
    def save(self, *args, **kwargs):
        if not self._validate_cartitem():
            return

        self._set_price()
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} {self.cart}"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    price = models.FloatField(blank=True, null=False, editable=False)
