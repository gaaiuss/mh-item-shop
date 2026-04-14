from typing import Any

from django.contrib.auth.models import User
from django.forms import CharField, ModelForm, PasswordInput

from user_profile.models import UserProfile


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        exclude = ("user",)  # type: ignore


class UserForm(ModelForm):
    password = CharField(required=False, widget=PasswordInput)

    def __init__(
        self,
        user: User | None = None,
        *args: Any,  # noqa: ANN401
        **kwargs: dict[str, Any],
    ) -> None:
        super().__init__(*args, **kwargs)

        self.user = user

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password", "email")

    def clean(self, *args: Any, **kwargs: dict[str, Any]) -> dict[str, Any]:  # noqa: ANN401
        super().clean(*args, **kwargs)
        data = self.data
        cleaned = self.cleaned_data

        print(data)

        return data
