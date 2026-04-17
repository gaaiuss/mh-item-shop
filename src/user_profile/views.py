# type: ignore
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from user_profile.forms import ProfileForm, UserForm
from user_profile.models import UserProfile


class BaseProfile(View):
    template_name = "user_profile/create.html"

    def setup(self, request: HttpRequest, *args: Any, **kwargs: dict[str, Any]) -> None:
        super().setup(request, *args, **kwargs)

        if self.request.user.is_authenticated:
            self.user_profile = UserProfile.objects.filter(
                user=self.request.user
            ).first()

            self.context = {
                "userform": UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user,
                ),
                "profileform": ProfileForm(data=self.request.POST or None),
            }
        else:
            self.context = {
                "userform": UserForm(data=self.request.POST or None),
                "profileform": ProfileForm(data=self.request.POST or None),
            }

        self.userform = self.context["userform"]
        self.profileform = self.context["profileform"]

        self.renderize = render(self.request, self.template_name, self.context)

    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:
        return self.renderize


class CreateProfile(BaseProfile):
    def post(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:
        if not self.userform.is_valid() or not self.userform.is_valid():
            print("INVALID")
            return self.renderize

        print("VALID")
        return self.renderize


class UpdateProfile(BaseProfile): ...


class Login(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:
        return HttpResponse("Login")


class Logout(View):
    def get(self, *args: Any, **kwargs: dict[str, Any]) -> HttpResponse:
        return HttpResponse("Logout")
