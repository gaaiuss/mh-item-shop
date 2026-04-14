from django.urls import path

from order.views import Detail, Pay, SaveOrder

app_name = "order"

urlpatterns = [
    path("pay/", Pay.as_view(), name="pay"),
    path("saveorder/", SaveOrder.as_view(), name="saveorder"),
    path("detail/", Detail.as_view(), name="detail"),
]
