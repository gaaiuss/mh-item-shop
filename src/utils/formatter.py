from typing import Any


def format_price(price: int) -> str:
    return f"{price}z"


def cart_total_amout(cart: dict[str, Any]) -> int:
    return sum([item["amount"] for item in cart.values()])


def cart_total_price(cart: dict[str, Any]) -> int:
    return sum(
        [
            item.get("amount_promo_price")
            if item.get("amount_promo_price")
            else item.get("amount_price")
            for item in cart.values()
        ]
    )
