from django.contrib import admin

from .models import Category, Product, ProductPictures, ProductVariant


class ProductPictureDisplay(admin.TabularInline):
    model = ProductPictures


class ProductVariantDisplay(admin.TabularInline):
    model = ProductVariant


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
        ProductPictureDisplay,
        ProductVariantDisplay
    ]
    readonly_fields = [
        'slug',
        'profit',
        'created_at',
        'sku'
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
