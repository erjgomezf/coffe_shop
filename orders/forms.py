from django.forms import Form, ModelForm
from .models import OrderProduct

class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['product']
        # You can add widgets and validation logic here as needed
    