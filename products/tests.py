from django.test import TestCase
from django.urls import reverse


# Create your tests here.

from django.contrib.auth import get_user_model

class ProductListViewTest(TestCase):

    # Test: usuario NO autenticado debe ser redirigido al login
    def test_redirects_to_login_if_not_authenticated(self):
        url = reverse("list_products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/usuarios/login/'))

    # Test: usuario autenticado puede ver la lista
    def test_authenticated_user_sees_list(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        url = reverse("list_products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
