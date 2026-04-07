from typing import TYPE_CHECKING

from django.contrib import admin

from user_profile.models import UserProfile

if TYPE_CHECKING:
    UserProfileModelAdmin = admin.ModelAdmin[UserProfile]
else:
    UserProfileModelAdmin = admin.ModelAdmin


@admin.register(UserProfile)
class UserProfileAdmin(UserProfileModelAdmin): ...
