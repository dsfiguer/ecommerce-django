from django.contrib import admin

from .models import Website


class WebsiteAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created_at',
        'is_available',
        'is_deleted'
    ]

    readonly_fields = [
        'created_at'
    ]


admin.site.register(Website, WebsiteAdmin)
