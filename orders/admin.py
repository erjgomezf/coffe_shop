from django.contrib import admin

# Register your models here.
from .models import Order, OrderProduct


class OrderProductInlineAdmin(admin.TabularInline):
    """
    Inline admin para gestionar productos dentro de una orden.
    Permite agregar, editar y eliminar productos asociados a una orden directamente desde la interfaz de administración de Django.
    Atributos:
        model: El modelo OrderProduct que representa los productos en la orden.
        extra: Número de formularios adicionales para agregar nuevos productos (0 significa ninguno).
    Uso:
        class OrderAdmin(admin.ModelAdmin):
            inlines = [OrderProductInlineAdmin]
    """

    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    """
    Admin para gestionar órdenes.
    Permite agregar, editar y eliminar órdenes desde la interfaz de administración de Django.
    Atributos:
        model: El modelo Order que representa las órdenes.
        inlines: Las vistas en línea que se mostrarán dentro del formulario de la orden.
    Uso:
        admin.site.register(Order, OrderAdmin)
    """

    model = Order
    inlines = [OrderProductInlineAdmin]


admin.site.register(Order, OrderAdmin)
