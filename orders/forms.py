from django.forms import Form, ModelForm
from .models import OrderProduct


class OrderProductForm(ModelForm):
    """
    Formulario para agregar productos a una orden.
    Permite seleccionar un producto para agregar a la orden del usuario.
    Atributos:
        model: El modelo OrderProduct que representa los productos en la orden.
        fields: Los campos del modelo que se mostrarán en el formulario.
    Uso:
        form = OrderProductForm()
        form.fields['product'].queryset = Product.objects.all()
        form.save(commit=False)
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
    """

    class Meta:
        model = OrderProduct
        fields = ["product"]
        # You can add widgets and validation logic here as needed
