from django.views.generic import DetailView
from .models import Order


# Create your views here.
class MyOrderView(DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(
            is_active=True
        ).first()  # Simula obtener el pedido del usuario actual
