from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from project import settings

urlpatterns = [
    path("", include("product.urls")),
    path("user_profile/", include("user_profile.urls")),
    path("order/", include("order.urls")),
    path("admin/", admin.site.urls),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *debug_toolbar_urls(),  # TODO(gaaiuss): Remove debug toolbar
]
