from itertools import product
import random

from django.db import models
from apps.cart.models import Cart

from apps.contact.models import ContactInfo
from apps.order.models import Order
from apps.website.models import Website
from apps.product.models import Product



class Ticket(models.Model):
    def gen_ticketnum():
        return str(random.randint(1000000000, 9999999999))
    
    def __str__(self):
        return self.ticket_number

    notes = models.TextField()
    resolved = models.BooleanField(default=False)

    ticket_number = models.CharField(
        max_length=10,
        default=gen_ticketnum(),
        editable=False,
        unique=True,
        primary_key=True
    )

class RelEmail(models.Model):
    def __str__(self):
        return self.email.__str__()

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    email = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)


class RelSite(models.Model):
    def __str__(self):
        return self.website.__str__()

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)


class RelProduct(models.Model):
    def __str__(self):
        return self.website.__str__()

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class RelOrder(models.Model):
    def __str__(self):
        return self.order.__str__()

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class RelCart(models.Model):
    def __str__(self):
        return self.cart.__str__()

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

