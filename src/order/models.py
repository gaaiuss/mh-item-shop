from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ("A", "Approved"),
            ("C", "Created"),
            ("F", "Failed"),
            ("P", "Pending"),
            ("S", "Sent"),
            ("F", "Finished"),
        ),
    )

    def __str__(self) -> str:
        return f"Order N. {self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=50)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promo_price = models.FloatField()
    amount = models.PositiveIntegerField()
    image = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return f"Item from {self.order}"
