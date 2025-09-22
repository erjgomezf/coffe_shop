from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class ProductListViewTest(TestCase):

    # Test para saber si la pagina responde codigo 200
    def test_should_return_200(self):
        url = reverse("list_products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
