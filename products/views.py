from django.views.generic import TemplateView, FormView
from products.forms import ProductForm
from products.models import Product
from django.urls import reverse_lazy


# Create your views here.
class ProductListView(TemplateView):
    """
    Vista para mostrar la lista de productos.
    Muestra todos los productos disponibles en la tienda de café.
    Uses the 'products/list_products.html' template.
    Args:
    - TemplateView: Vista basada en plantillas de Django.
    Methods:
    - get_context_data: Agrega la lista de productos al contexto de la plantilla.
    Returns:
    - dict: Contexto actualizado con la lista de productos.
    """

    template_name = "products/list_products.html"

    def get_context_data(self, **kwargs) -> dict:
        """
        Agrega la lista de productos al contexto de la plantilla.
        Retorna el contexto actualizado.
        Args:
        - **kwargs: Argumentos adicionales.
        Returns:
        - dict: Contexto actualizado con la lista de productos.
        """
        context = super().get_context_data(**kwargs)
        context["list_products"] = Product.objects.all()
        return context


class ProductFormView(FormView):
    """
    Vista para agregar un nuevo producto.
    Permite a los administradores agregar nuevos productos a la tienda de café.
    Uses the 'products/add_product.html' template and ProductForm.
    Args:
    - FormView: Vista basada en formularios de Django.
    Attributes:
    - template_name: Nombre de la plantilla HTML.
    - form_class: Clase del formulario para agregar productos.
    - success_url: URL a la que redirige después de agregar un producto.
    Methods:
    - form_valid: Guarda el producto si el formulario es válido y redirige a la lista de productos.
    Returns:
    - HttpResponseRedirect: Redirección a la lista de productos.
    Usage in URLconf:
        path('add-product/', ProductFormView.as_view(), name='add_product')
    """

    template_name = "products/add_product.html"  # Plantilla para agregar un producto
    form_class = ProductForm  # Formulario para agregar un producto
    success_url = reverse_lazy(
        "list_products"
    )  # Redirige a la lista de productos después de agregar uno nuevo

    def form_valid(self, form) -> None:
        """
        Guarda el producto si el formulario es válido y redirige a la lista de productos.
        Args:
        - form: Instancia del formulario válido.
        Returns:
        - HttpResponseRedirect: Redirección a la lista de productos.
        """
        form.save()
        return super().form_valid(form)
