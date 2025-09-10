from django import forms
from products.models import Product


class ProductForm(forms.Form):
    """
    Formulario para agregar un nuevo producto.
    Incluye campos para el nombre, descripción, precio, stock e imagen del producto.
    Args:
    - forms.Form: Formulario de Django.
    Methods:
    - save: Guarda el producto en la base de datos.
    Returns:
    - None
    """

    name = forms.CharField(max_length=100, label="Nombre del Producto")
    description = forms.CharField(
        widget=forms.Textarea, label="Descripción del Producto"
    )
    price = forms.DecimalField(
        max_digits=10, decimal_places=2, label="Precio del Producto"
    )
    stock = forms.IntegerField(label="Cantidad en Stock del Producto")
    image = forms.ImageField(label="Imagen del Producto", required=False)

    def save(self):
        # Aquí iría la lógica para guardar el producto en la base de datos
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            stock=self.cleaned_data["stock"],
            image=self.cleaned_data.get("image"),
        )
