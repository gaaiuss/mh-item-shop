from django.template import Library

from utils import formatter

register = Library()


@register.filter
def format_price(price: int) -> str:
    return formatter.format_price(price)
