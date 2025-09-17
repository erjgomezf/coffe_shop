from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin   # Asegura que el usuario esté autenticado
from django.urls import reverse_lazy    # Para redirecciones basadas en nombres de URL
from django.shortcuts import redirect
from django.contrib import messages
from django.db import transaction
from .models import Order, OrderProduct
from products.models import Product


# Create your views here.
class MyOrderView(LoginRequiredMixin, DetailView):
    '''
    Vista para mostrar el pedido actual del usuario.
    Muestra los detalles del pedido activo asociado al usuario autenticado.
    Atributos:
        model: El modelo Order que representa los pedidos.
        template_name: La plantilla HTML utilizada para renderizar la vista.
        context_object_name: El nombre del contexto para acceder al pedido en la plantilla.
    Método:
        get_object: Sobrescribe el método para obtener el pedido activo del usuario actual. 
    Uso en URLconf:
        path('my-order/', MyOrderView.as_view(), name='my_order')
    '''

    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(
            is_active=True, user=self.request.user
        ).first()  # Simula obtener el pedido del usuario actual

class CreateOrderProductView(LoginRequiredMixin, View):
    '''
    Endpoint para agregar (o incrementar) un producto a la orden activa del usuario.
    Espera un POST con el campo 'product' (ID del producto). Si ya existe en la orden,
    incrementa la cantidad; de lo contrario, lo crea con cantidad 1. Siempre redirige a "my_order".
    '''

    success_url = reverse_lazy("my_order")

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("product")
        if not product_id:
            messages.error(request, "No se especificó un producto válido.")
            return redirect(self.success_url)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            messages.error(request, "El producto seleccionado no existe.")
            return redirect(self.success_url)

        order, _ = Order.objects.get_or_create(user=request.user, is_active=True)

        order_product, created = OrderProduct.objects.get_or_create(
            order=order, product=product, defaults={"quantity": 0}
        )
        order_product.quantity = (order_product.quantity or 0) + 1
        order_product.save()

        messages.success(request, f"Se agregó {product.name} a tu pedido.")
        return redirect(self.success_url)