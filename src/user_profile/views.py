from typing import Any

from django.http import HttpResponse
from django.views import View


class CreateProfile(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("CreateProfile")


class UpdateProfile(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("UpdateProfile")


class Login(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("Login")


class Logout(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:  # noqa: ANN401
        return HttpResponse("Logout")
