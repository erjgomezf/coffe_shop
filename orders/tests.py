from django.contrib.auth import get_user_model
from .models import Order
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your tests here.
class MyOrderViewTest(TestCase):

    # Set up inicial para crear un usuario y una orden
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username="testuser", password="testpass"
        )
        self.order = Order.objects.create(user=self.user, is_active=True)

    # Test para saber si un usuario NO autenticado es redirigido a login
    def test_redirects_to_login_if_not_authenticated(self):
        url = reverse("my_order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/usuarios/login/"))

    # Test para saber si un usuario autenticado puede ver su orden
    def test_authenticated_user_sees_order(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse("my_order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Orden #1")
        self.assertContains(response, "testuser")

    # Test para saber si la pagina con usuario autenticado responde codigo 200 forzando login
    def test_should_return_200(self):
        url = reverse("my_order")
        user = get_user_model().objects.create_user(username="test")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
