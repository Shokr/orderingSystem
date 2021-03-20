from django.test import TestCase
from orders.models import Order
from orders.tests.factories import OrderFactory


class TestProductsMode(TestCase):
    def test_create_product(self):
        OrderFactory.create_batch(3)
        self.assertEqual(Order.objects.count(), 3)