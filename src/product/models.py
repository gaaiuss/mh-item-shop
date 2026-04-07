from typing import Any

from django.db import models

from utils.images import resize_image


class Product(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.TextField(max_length=100)
    description = models.TextField(max_length=255)
    image = models.ImageField(
        upload_to="product_images/%Y/%m/", blank=False, null=False
    )
    slug = models.SlugField(unique=True)
    market_price = models.FloatField()
    promo_market_price = models.FloatField(default=0)
    product_type = models.CharField(
        default="V", max_length=1, choices=(("V", "Variation"), ("S", "Simple"))
    )

    def save(self, *args: Any, **kwargs: dict[str, Any]) -> None:  # noqa: ANN401
        super().save(*args, **kwargs)

        if self.image:
            resize_image(self.image)

    def __str__(self) -> str:
        return self.name


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    promo_price = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name or self.product.name
