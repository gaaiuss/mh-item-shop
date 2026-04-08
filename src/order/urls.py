from django.urls import path

from order.views import CloseOrder, Detail, Pay

app_name = "order"

urlpatterns = [
    path("pay/", Pay.as_view(), name="pay"),
    path("closeorder/", CloseOrder.as_view(), name="closeorder"),
    path("detail/", Detail.as_view(), name="detail"),
]
