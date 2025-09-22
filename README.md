# ☕ Coffee Shop

Proyecto web de gestión de productos y pedidos para una tienda de café, desarrollado con Django 5, PostgreSQL y Tailwind CSS.

## Características principales

- Gestión de productos (CRUD)
- Gestión de usuarios (registro, login, logout)
- Pedidos y carrito de compras
- API REST para productos y pedidos
- Interfaz moderna y responsive con Tailwind CSS

## Requisitos

- Python 3.10+
- PostgreSQL 13+
- pip
- Entorno virtual recomendado (`venv`)

## Instalación y configuración

1. **Clona el repositorio:**
   ```bash
   git clone <URL-del-repo>
   cd coffe_shop
   ```
2. **Crea y activa un entorno virtual:**
   ```bash
   python3 -m venv ~/.envs/coffe_shop
   source ~/.envs/coffe_shop/bin/activate
   ```
3. **Instala dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configura la base de datos PostgreSQL:**
   - Crea la base de datos y usuario:
     ```sql
     CREATE DATABASE coffe_shop;
     CREATE USER postgres WITH PASSWORD 'Postgres';
     GRANT ALL PRIVILEGES ON DATABASE coffe_shop TO postgres;
     ```
   - Edita `coffe_shop/settings.py` en la sección `DATABASES`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'coffe_shop',
             'USER': 'postgres',
             'PASSWORD': 'Postgres',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```
5. **Aplica migraciones:**
   ```bash
   python manage.py migrate
   ```
6. **Crea un superusuario (opcional):**
   ```bash
   python manage.py createsuperuser
   ```
7. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

## Pruebas

Para ejecutar los tests automatizados:

```bash
python manage.py test
```

## Estructura del proyecto

- `products/` — Gestión de productos
- `orders/` — Pedidos y carrito
- `users/` — Autenticación y usuarios
- `templates/` — Plantillas HTML base
- `static/` — Archivos estáticos (si aplica)

## Créditos

Desarrollado por erjgomezf y colaboradores.

---

> ¿Dudas o sugerencias? ¡Abre un issue o contacta al autor!
