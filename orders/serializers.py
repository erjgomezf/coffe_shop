from rest_framework.serializers import ModelSerializer
from .models import Order, OrderProduct


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = "__all__"
