from django.views.generic import (
    FormView,
    ListView,
)  # Vistas genéricas basadas en clases
from django.urls import reverse_lazy  # Para redirecciones basadas en nombres de URL
from rest_framework.views import APIView  # Vista base para APIs
from rest_framework.response import Response  # Respuesta para APIs
from products.forms import ProductForm  # Formulario para agregar productos
from products.models import Product  # Modelo de Producto
from .serializers import ProductSerializer  # Serializador para el modelo Product


# Create your views here.
class ProductFormView(FormView):
    """
    Vista para agregar un nuevo producto.
    Permite a los usuarios agregar nuevos productos a la tienda.
    Atributos:
        template_name: La plantilla HTML utilizada para renderizar el formulario.
        form_class: El formulario utilizado para agregar productos.
        success_url: La URL a la que se redirige después de agregar el producto.
    Método:
        form_valid: Sobrescribe el método para manejar la lógica de agregar el producto.
    Uso en URLconf:
        path('agregar/', ProductFormView.as_view(), name='add_product')
    """

    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("list_products")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(ListView):
    """
    Vista para listar productos.
    Muestra una lista de productos disponibles en la tienda.
    Atributos:
        model: El modelo Product que representa los productos.
        template_name: La plantilla HTML utilizada para renderizar la vista.
        context_object_name: El nombre del contexto para acceder a la lista de productos en la plantilla.
    Uso en URLconf:
        path('', ProductListView.as_view(), name='list_products')
    """

    model = Product
    template_name = "products/list_products.html"
    context_object_name = "products"


class ProductListAPI(APIView):
    """
    API para listar productos.
    Proporciona una API RESTful para obtener una lista de productos en formato JSON.
    Atributos:
        authentication_classes: Clases de autenticación utilizadas (vacío para acceso público).
        permission_classes: Clases de permiso utilizadas (vacío para acceso público).
    Método:
        get: Maneja la solicitud GET para obtener la lista de productos.
    Uso en URLconf:
        path('api/', ProductListAPI.as_view(), name='list_products_api')
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request) -> Response:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
