from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField


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


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=50)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promo_price = models.FloatField()
    amount = models.PositiveIntegerField()
    image = CharField()
