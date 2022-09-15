from django.contrib import admin

from .models import ContactInfo


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'created_at',
        'responded'
    ]
    readonly_fields = [
        'created_at'
    ]


admin.site.register(ContactInfo, ContactAdmin)
