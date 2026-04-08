from typing import Any

from django.http import HttpResponse
from django.views import View


class Pay(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("Pay")


class CloseOrder(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("CloseOrder")


class Detail(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("Detail")
