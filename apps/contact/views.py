from rest_framework import generics

from .serializers import ContactFormSerializer


class ContactForm(generics.CreateAPIView):
    serializer_class = ContactFormSerializer
