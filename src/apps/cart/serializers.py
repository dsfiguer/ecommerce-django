from rest_framework import serializers

from .models import Cart, CartItem


class CreateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'product',
            'cart'
        ]


class CreateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'discount'
        ]
