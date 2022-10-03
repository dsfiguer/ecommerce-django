import email
from rest_framework import serializers

from .models import ContactInfo


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = [
            'site',
            'first_name',
            'last_name',
            'email',
            'note'
        ]
