from django.views.generic import TemplateView, FormView
from products.forms import ProductForm
from products.models import Product
from django.urls import reverse_lazy


# Create your views here.
class ProductListView(TemplateView):
    """
    Vista para mostrar la lista de productos.
    Muestra todos los productos disponibles en la tienda de café.
    Uses the 'products/product_list.html' template.
    Args:
    - TemplateView: Vista basada en plantillas de Django.
    Methods:
    - get_context_data: Agrega la lista de productos al contexto de la plantilla.
    Returns:
    - dict: Contexto actualizado con la lista de productos.
    """

    template_name = "products/product_list.html"

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
        context["product_list"] = Product.objects.all()
        return context


class ProductFormView(FormView):
    """
    Vista para agregar un nuevo producto.
    Muestra un formulario para agregar un nuevo producto a la tienda de café.
    Uses the 'products/add_product.html' template and ProductForm form class.
    Args:
    - FormView: Vista basada en formularios de Django.
    Methods:
    - form_valid: Guarda el producto si el formulario es válido y redirige a la lista de productos.
    Returns:
    - HttpResponseRedirect: Redirección a la lista de productos si el formulario es válido.
    """

    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

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
