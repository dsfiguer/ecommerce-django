from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number',
        'placed',
        'shipped',
        'refund'
    ]
    
    readonly_fields = [
        'full_address',
        'order_number',
        'placed'
    ]


admin.site.register(Order, OrderAdmin)
