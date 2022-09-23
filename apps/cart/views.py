from rest_framework import generics

from .models import CartItem
from .serializers import (
    CreateCartItemSerializer, CreateCartSerializer
)


class CreateCartItem(generics.CreateAPIView):
    serializer_class = CreateCartItemSerializer


class DestroyCartItem(generics.DestroyAPIView):
    
    def get_object(self):
        item_pk = self.kwargs.get('id')
        return CartItem.objects.get(id=item_pk)


class CreateCart(generics.CreateAPIView):
    serializer_class = CreateCartSerializer
