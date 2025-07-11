from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    "Show various Order attributes in admin table."

    list_display = ("order_id", "marketplace", "order_status", "order_purchase_date")


admin.site.register(Order, OrderAdmin)
