from rest_framework import serializers

from .models import Order


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'site',
            'cart',
            'referral',
            'referral_source',
            'email',
            'first_name',
            'last_name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zipcode'
        ]
