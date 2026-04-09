from typing import Any

from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView

from product.models import Product

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
