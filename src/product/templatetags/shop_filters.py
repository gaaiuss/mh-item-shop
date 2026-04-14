from typing import Any

from django.template import Library

from utils import formatter

register = Library()


@register.filter
def format_price(price: int) -> str:
    return formatter.format_price(price)


@register.filter
def cart_total_amout(cart: dict[str, Any]) -> int:
    return formatter.cart_total_amout(cart)


@register.filter
def cart_total_price(cart: dict[str, Any]) -> int:
    return formatter.cart_total_price(cart)
