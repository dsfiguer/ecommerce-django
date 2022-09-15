from django.contrib import admin

from .models import RelCart, RelEmail, RelOrder, RelProduct, RelSite, Ticket


class RelEmailDisplay(admin.TabularInline):
    model = RelEmail


class RelSiteDisplay(admin.TabularInline):
    model = RelSite


class RelProductDisplay(admin.TabularInline):
    model = RelProduct


class RelOrderDisplay(admin.TabularInline):
    model = RelOrder


class RelCartDisplay(admin.TabularInline):
    model = RelCart


class TicketAdmin(admin.ModelAdmin):
    list_display = [
        'ticket_number',
        'resolved'
    ]
    inlines = [
        RelEmailDisplay,
        RelSiteDisplay,
        RelProductDisplay,
        RelOrderDisplay,
        RelCartDisplay
    ]
    readonly_fields = [
        'ticket_number'
    ]


admin.site.register(Ticket, TicketAdmin)
