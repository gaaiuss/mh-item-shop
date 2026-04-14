from django.urls import path

from user_profile.views import CreateProfile, Login, Logout, UpdateProfile

app_name = "user_profile"

urlpatterns = [
    path("", CreateProfile.as_view(), name="create"),
    path("update/", UpdateProfile.as_view(), name="update"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
