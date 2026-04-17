from typing import Any

from django.contrib.auth.models import User
from django.forms import CharField, ModelForm, PasswordInput, ValidationError

from user_profile.models import UserProfile


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        exclude = ("user",)


class UserForm(ModelForm):
    password = CharField(required=False, widget=PasswordInput)
    password2 = CharField(required=False, widget=PasswordInput, label="Repeat Password")

    def __init__(
        self,
        user: User | None = None,
        *args: Any,
        **kwargs: dict[str, Any],
    ) -> None:
        super().__init__(*args, **kwargs)

        self.user = user

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
        )

    def clean(self) -> None:  # type: ignore
        cleaned = self.cleaned_data
        validation_error_msg: dict[str, Any] = {}

        user_data = cleaned.get("username")
        email_data = cleaned.get("email")
        password_data: str | Any = cleaned.get("password")
        password2_data = cleaned.get("password2")

        user_db = User.objects.filter(username=user_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = "User already exists"
        error_msg_email_exists = "Email already exists"
        error_msg_password_match = "Passwords does not match"
        error_msg_password_short = (
            "Password is too short. It needs a least 6 characters"
        )
        error_msg_required_field = "Required field"
        # Logged User
        if self.user:
            if user_db and user_data != user_db.username:
                validation_error_msg["username"] = error_msg_user_exists

            if email_db and email_data != email_db.email:
                validation_error_msg["email"] = error_msg_email_exists

            if password_data and password_data != password2_data:
                validation_error_msg["password"] = error_msg_password_match
                validation_error_msg["password2"] = error_msg_password_match

            if len(password_data) < 6:
                validation_error_msg["password"] = error_msg_password_short
        # New User
        else:
            if user_db:
                validation_error_msg["username"] = error_msg_user_exists

            if email_db:
                validation_error_msg["email"] = error_msg_email_exists

            if not password_data:
                validation_error_msg["password"] = error_msg_required_field

            if not password2_data:
                validation_error_msg["password2"] = error_msg_required_field

            if password_data != password2_data:
                validation_error_msg["password"] = error_msg_password_match
                validation_error_msg["password2"] = error_msg_password_match

            if len(password_data) < 6:
                validation_error_msg["password"] = error_msg_password_short

        if validation_error_msg:
            raise ValidationError(validation_error_msg)
