from django.contrib import admin

from .models import Product, ProductPictures


class ProductPictureDisplay(admin.TabularInline):
    model = ProductPictures


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'site',
        'sku',
        'name',
        'price',
        'profit',
        'is_available'
    ]
    inlines = [
        ProductPictureDisplay
    ]
    readonly_fields = [
        'slug',
        'profit',
        'created_at',
        'sku'
    ]


admin.site.register(Product, ProductAdmin)
