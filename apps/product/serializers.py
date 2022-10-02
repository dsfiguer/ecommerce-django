from rest_framework import serializers

from .models import Product, ProductPictures, ProductVariant


class ProductPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPictures
        fields = [
            'picture',
            'thumbnail'
        ]


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = [
            'title',
            'price'
        ]


class ListProductSerializer(serializers.ModelSerializer):
    pics = ProductPictureSerializer(many=True, read_only=True)
    variant = ProductVariantSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            'sku',
            'name',
            'price',
            'pics',
            'variant'
        ]
