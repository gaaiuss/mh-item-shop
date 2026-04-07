from typing import TYPE_CHECKING

from django.contrib import admin

from order.models import Order, OrderItem

if TYPE_CHECKING:
    OrderModelAdmin = admin.ModelAdmin[Order]
    OrderItemModelAdmin = admin.ModelAdmin[OrderItem]
else:
    OrderModelAdmin = admin.ModelAdmin
    OrderItemModelAdmin = admin.ModelAdmin


@admin.register(Order)
class OrderAdmin(OrderModelAdmin): ...


@admin.register(OrderItem)
class OrderItemAdmin(OrderItemModelAdmin): ...
