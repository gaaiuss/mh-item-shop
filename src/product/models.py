from typing import Any

from django.db import models
from django.utils.text import slugify

from utils.formatter import format_price
from utils.images import resize_image


class Product(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.TextField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(
        upload_to="product_images/%Y/%m/", blank=False, null=False
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    market_price = models.PositiveIntegerField()
    promo_market_price = models.PositiveIntegerField(default=0)
    product_type = models.CharField(
        default="V", max_length=1, choices=(("V", "Variable"), ("S", "Simple"))
    )

    def get_fomatted_market_price(self) -> str:
        return format_price(self.market_price)

    get_fomatted_market_price.short_description = "Price"  # type: ignore

    def get_fomatted_promo_market_price(self) -> str:
        return format_price(self.promo_market_price)

    get_fomatted_promo_market_price.short_description = "Promo Price"  # type: ignore

    def save(self, *args: Any, **kwargs: dict[str, Any]) -> None:  # noqa: ANN401
        if not self.slug:
            self.slug = f"{slugify(self.name)}"

        super().save(*args, **kwargs)

        if self.image:
            resize_image(self.image)

    def __str__(self) -> str:
        return self.name


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.PositiveIntegerField()
    promo_price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name or self.product.name
