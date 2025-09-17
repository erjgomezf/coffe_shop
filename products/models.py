from django.db import models


# Create your models here.
class Product(models.Model):
    """
    Modelo para representar un producto en la tienda de café.
    Fields:
    - name: Nombre del producto.
    - description: Descripción del producto.
    - price: Precio del producto.
    - stock: Cantidad en stock del producto.
    - image: Imagen del producto.
    Methods:
    - __str__: Representación en cadena del producto.
    """

    name = models.CharField(
        max_length=100, verbose_name="Nombre del Producto"
    )  # Agregado verbose_name
    description = models.TextField(verbose_name="Descripción del Producto")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio del Producto"
    )
    stock = models.IntegerField(verbose_name="Cantidad en Stock del Producto")
    image = models.ImageField(
        upload_to="products/img/", verbose_name="Imagen del Producto", blank=True, null=True
    )

    def __str__(self):
        return self.name
