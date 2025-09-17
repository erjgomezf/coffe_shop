from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "stock", "image"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full rounded-lg border border-gray-300 px-4 py-2 shadow-sm focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 focus:outline-none transition bg-gray-50"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full rounded-lg border border-gray-300 px-4 py-2 shadow-sm focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 focus:outline-none transition bg-gray-50",
                    "rows": 3,
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "pl-7 w-full rounded-lg border border-gray-300 px-4 py-2 shadow-sm focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 focus:outline-none transition bg-gray-50",
                    "step": "0.01",
                    "min": "0",
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "class": "w-full rounded-lg border border-gray-300 px-4 py-2 shadow-sm focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 focus:outline-none transition bg-gray-50"
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "w-full rounded-lg border border-gray-300 px-4 py-2 shadow-sm focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 focus:outline-none transition bg-gray-50"
                }
            ),
        }
