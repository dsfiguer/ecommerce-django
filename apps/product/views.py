from rest_framework import generics
from django.shortcuts import get_object_or_404

from apps.website.models import Website
from .models import Product
from .serializers import ListProductSerializer


class ListSiteProducts(generics.ListAPIView):
    serializer_class = ListProductSerializer
    
    def get_queryset(self):
        website_name = self.kwargs.get('name')
        if "-" in website_name:
            website_name = website_name.replace("-", " ")

        website = get_object_or_404(Website, name=website_name)

        return Product.objects.filter(site=website, is_available=True)
