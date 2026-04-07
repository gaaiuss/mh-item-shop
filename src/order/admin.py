from typing import TYPE_CHECKING

from django.contrib import admin

from order.models import Order, OrderItem

if TYPE_CHECKING:
    OrderModelAdmin = admin.ModelAdmin[Order]
    OrderItemModelAdmin = admin.ModelAdmin[OrderItem]
    OrderItemInLineModelAdmin = admin.TabularInline[OrderItem]
else:
    OrderModelAdmin = admin.ModelAdmin
    OrderItemModelAdmin = admin.ModelAdmin
    OrderItemInLineModelAdmin = admin.TabularInline


class OrderItemInLine(OrderItemInLineModelAdmin):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(OrderModelAdmin):
    def __init__(self, model: type[Order], admin_site: admin.AdminSite) -> None:
        super().__init__(model, admin_site)
        self.inlines = [OrderItemInLine]


@admin.register(OrderItem)
class OrderItemAdmin(OrderItemModelAdmin): ...
