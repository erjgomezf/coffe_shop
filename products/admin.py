from django.contrib import admin
from products.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("name", "price", "stock")
    search_fields = ("name",)
    list_filter = ("price", "stock")


admin.site.register(Product, ProductAdmin)
