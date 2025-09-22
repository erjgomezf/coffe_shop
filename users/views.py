from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class RegisterView(generic.CreateView):
    """
    Vista para registrar nuevos usuarios.
    Utiliza el formulario incorporado UserCreationForm de Django para manejar el registro de usuarios.
    Atributos:
        form_class: El formulario utilizado para registrar nuevos usuarios.
        template_name: La plantilla HTML utilizada para renderizar la vista.
        success_url: La URL a la que se redirige después de un registro exitoso
    Uso en URLconf:
        path('register/', RegisterView.as_view(), name='register')
    """

    form_class = UserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
