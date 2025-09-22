from django.urls import path
from .views import MyOrderView, CreateOrderProductView
from .views import OrderProductAPI

urlpatterns = [
    path("mi-orden/", MyOrderView.as_view(), name="my_order"),
    path(
        "crear-orden-producto/",
        CreateOrderProductView.as_view(),
        name="create_order_product",
    ),
    path("api/", OrderProductAPI.as_view(), name="order_product_api"),
]
