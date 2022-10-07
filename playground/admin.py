from django.contrib import messages

from django.contrib import admin
from playground.models import Company, Event, Ticket

# admin.site.register()
# Register your models here.

from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from playground.models import Event, Ticket, Company


# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if form.cleaned_data["ticket_count"] < form.initial["ticket_count"]:
            messages.warning(
                request,
                f"Ticket count should be greater than initial value, so we set it to {form.initial['ticket_count']}",
            )
        super().save_model(request, obj, form, change)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("number", "get_username", "vip")
    list_filter = ("vip",)
    search_fields = ("event__title", "user__username")

    def get_username(self, obj: Ticket):
        empty_value = "---"
        username = getattr(obj.user, "username", empty_value)

        if username != empty_value:
            url = reverse(
                f'admin:{obj.user._meta.app_label}_{obj.user._meta.model_name}_change',
                args=[obj.user.id],
            )
            username = mark_safe(f"<a href={url}>{username}</a>")

        return username

    get_username.short_description = "username"
