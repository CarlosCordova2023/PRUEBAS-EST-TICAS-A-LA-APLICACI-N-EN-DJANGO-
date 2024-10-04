from django.test import TestCase
from django.urls import reverse

class ProductoTests(TestCase):
    def test_insertar_url_status_code(self):
        response = self.client.get('/fabrica/agregar/')
        self.assertEqual(response.status_code, 200)

    def test_insertar_url_by_name(self):
        url = reverse('agregar_producto')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_insertar_template_used(self):
        url = reverse('agregar_producto')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'fabrica/agregar_producto.html')

    def test_insertar_template_content(self):
        url = reverse('agregar_producto')
        response = self.client.get(url)
        self.assertContains(response, '<title>Agregar Producto</title>')
