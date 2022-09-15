from django.contrib import admin

from .models import Cart, CartItem, Discount


class CartItemDisplay(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = [
        'created_at',
        'total_profit'
    ]
    inlines = [
        CartItemDisplay,
    ]
    readonly_fields = [
        'total_price',
        'discounted_amount',
        'total_profit',
        'created_at'
    ]


class DiscountAdmin(admin.ModelAdmin):
    list_display = [
        'site',
        'percentage',
        'code'
    ]


admin.site.register(Cart, CartAdmin)
admin.site.register(Discount, DiscountAdmin)
