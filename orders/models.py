from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class Order(models.Model):
    """
    Modelo que representa una orden de compra.
    Atributos:
    - user: Usuario que realizó la orden.
    - is_active: Indica si la orden está activa.
    - order_date: Fecha y hora en que se realizó la orden.
    Métodos:
    - get_total: Calcula el total de la orden sumando los precios de los productos en la orden.
    - __str__: Devuelve una representación en cadena de la orden.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        total = 0
        for order_product in self.orderproduct_set.all():
            total += order_product.product.price * order_product.quantity
        return total

    def __str__(self):
        return f"Order {self.id} by {self.user}"


class OrderProduct(models.Model):
    """
    Modelo que representa un producto en una orden de compra.
    Atributos:
    - order: Orden a la que pertenece el producto.
    - product: Producto que se ha añadido a la orden.
    - quantity: Cantidad del producto en la orden.
    Métodos:
    - __str__: Devuelve una representación en cadena del producto en la orden.
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"
