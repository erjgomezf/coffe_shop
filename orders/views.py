from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin   # Asegura que el usuario esté autenticado
from django.urls import reverse_lazy    # Para redirecciones basadas en nombres de URL
from django.shortcuts import redirect
from django.contrib import messages
from django.db import transaction
from .models import Order, OrderProduct
from .forms import OrderProductForm
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

class CreateOrderProductView(LoginRequiredMixin, CreateView):
    '''
    Vista para agregar un producto a la orden del usuario.
    Permite a los usuarios autenticados agregar productos a su orden activa.
    Atributos:
        template_name: La plantilla HTML utilizada para renderizar el formulario.
        form_class: El formulario utilizado para agregar productos a la orden.
        success_url: La URL a la que se redirige después de agregar el producto.
    Método:
        form_valid: Sobrescribe el método para manejar la lógica de agregar el producto a la orden.
    Uso en URLconf:
        path('add-to-order/', CreateOrderProductView.as_view(), name='add_to_order')
    '''
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("my_order")

    
    
    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(is_active=True, user=self.request.user)
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        messages.success(self.request, "Producto agregado a la orden.")
        return super().form_valid(form)