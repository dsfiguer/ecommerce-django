from rest_framework import generics

from .serializers import CreateOrderSerializer


class CreateOrder(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer
