from django.test import TestCase
from products.models import Product
from products.tests.factories import ProductFactory


class TestProductsMode(TestCase):
    def test_create_product(self):
        ProductFactory.create()
        self.assertEqual(Product.objects.count(), 1)
