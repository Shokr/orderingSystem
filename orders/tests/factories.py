import factory

from orders.models import Order
from products.tests.factories import ProductFactory
from users.tests.factories import CustomerFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
    product = factory.SubFactory(ProductFactory)
    qty = factory.Sequence(int)
