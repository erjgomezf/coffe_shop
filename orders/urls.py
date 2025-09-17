from django.urls import path
from .views import MyOrderView, CreateOrderProductView


urlpatterns = [
    path("mi-orden/", MyOrderView.as_view(), name="my_order"),
    path("crear-orden-producto/", CreateOrderProductView.as_view(), name="create_order_product"),
]
