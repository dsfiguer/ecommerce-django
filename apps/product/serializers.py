from dataclasses import field
from rest_framework import serializers

from .models import Product


class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
