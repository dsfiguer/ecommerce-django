from rest_framework import serializers

from .models import Product, ProductPictures


class ProductPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPictures
        fields = [
            'picture',
            'thumbnail'
        ]

class ListProductSerializer(serializers.ModelSerializer):
    pics = ProductPictureSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            'sku',
            'name',
            'price',
            'pics'
        ]
