from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from .forms import OrderProductForm
from django.urls import reverse_lazy


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

class CreateOrderProductView(LoginRequiredMixin, DetailView):
    '''
    Vista para agregar un producto a la orden del usuario.
    Permite a los usuarios autenticados agregar productos a su orden activa.
    Atributos:
        template_name: La plantilla HTML utilizada para renderizar la vista.
        form_class: El formulario utilizado para agregar productos a la orden.
        success_url: La URL a la que se redirige después de agregar un producto exitosamente.
    Método:
        form_valid: Sobrescribe el método para manejar la lógica de agregar el producto a la orden.
    Uso en URLconf:
        path('add-product/', CreateOrderProductView.as_view(), name='add_product_to_order')
    '''
    
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm  # Aquí deberías definir el formulario para agregar productos a la orden
    success_url = reverse_lazy("my_order")
    
    def form_valid(self, form):
        '''
        Maneja la lógica para agregar un producto a la orden del usuario.
        Si la orden activa no existe, la crea. Luego, agrega el producto con la cantidad predeterminada de 1.
        Args:
            form: El formulario que contiene los datos del producto a agregar.
        Returns:
            Redirige a la URL de éxito definida.    
        '''
        order, _ = Order.objects.get_or_create(user=self.request.user, is_active=True)
        form.instance.order = order
        form.instance.quantity = 1  # Puedes ajustar esto según tus necesidades
        form.save()
        return super().form_valid(form)