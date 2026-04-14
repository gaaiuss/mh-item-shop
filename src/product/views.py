from typing import Any

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView

from product.models import Product, Variation

PER_PAGE = 9


class ProductList(ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "products"
    paginate_by = PER_PAGE


class ProductDetail(DetailView):
    model = Product
    template_name = "product/detail.html"
    context_object_name = "product"
    slug_url_kwarg = "slug"


class AddToCart(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        http_referer = self.request.META.get("HTTP_REFERER", reverse("product:list"))
        variation_id = self.request.GET.get("vid")

        if not variation_id:
            messages.error(self.request, "Product does not exists")
            return redirect(http_referer)

        variation = get_object_or_404(Variation, id=variation_id)
        variation_stock = variation.stock
        product = variation.product

        product_id = product.id  # type: ignore
        product_name = product.name
        variation_name = variation.name or ""
        unit_price = variation.price
        promo_unit_price = variation.promo_price
        slug = product.slug
        image = product.image.name if product.image else ""

        if variation.stock < 1:
            messages.error(self.request, "Insufficient stock")
            return redirect(http_referer)

        if not self.request.session.get("cart"):
            self.request.session["cart"] = {}
            self.request.session.save()

        cart = self.request.session["cart"]

        if variation_id in cart:
            cart_amount = cart[variation_id]["amount"]
            cart_amount += 1

            if variation_stock < cart_amount:
                messages.warning(
                    self.request,
                    f"Insufficient stock for {cart_amount}x for the product "
                    f"'{product_name}'. We added {variation_stock}x in your cart",
                )
                cart_amount = variation_stock

            cart[variation_id]["amount"] = cart_amount
            cart[variation_id]["amount_price"] = unit_price * cart_amount
            cart[variation_id]["amount_promo_price"] = promo_unit_price * cart_amount
        else:
            cart[variation_id] = {
                "product_id": product_id,
                "product_name": product_name,
                "variation_name": variation_name,
                "variation_id": variation_id,
                "unit_price": unit_price,
                "promo_unit_price": promo_unit_price,
                "amount_price": unit_price,
                "amount_promo_price": promo_unit_price,
                "amount": 1,
                "slug": slug,
                "image": image,
            }

        self.request.session.save()

        messages.success(
            self.request,
            f"{product_name} ({cart[variation_id]['amount']}x) added successfully!",
        )

        return redirect(http_referer)


class RemoveFromCart(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        http_referer = self.request.META.get("HTTP_REFERER", reverse("product:list"))
        variation_id = self.request.GET.get("vid")

        if not variation_id:
            return redirect(http_referer)

        if not self.request.session.get("cart"):
            return redirect(http_referer)

        if variation_id not in self.request.session["cart"]:
            return redirect(http_referer)

        cart = self.request.session["cart"][variation_id]

        messages.success(self.request, f"{cart['product_name']} removed from your cart")

        del self.request.session["cart"][variation_id]
        self.request.session.save()

        return redirect(http_referer)


class Cart(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        context = {"cart": self.request.session.get("cart", {})}
        return render(self.request, "product/cart.html", context)


class OrderSummary(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("OrderSummary")
