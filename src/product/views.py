from typing import Any

from django.http import HttpResponse
from django.views import View


class ProductList(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("ProductList")


class ProductDetail(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("ProductDetail")


class AddToCart(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("AddToCart")


class RemoveFromCart(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("RemoveFromCart")


class Cart(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("Cart")


class Finish(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("Finish")
