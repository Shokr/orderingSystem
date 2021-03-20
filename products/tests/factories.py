import factory
from factory.django import DjangoModelFactory

from products.models import Product


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('sentence', nb_words=3)
    slug = factory.Faker('sentence', nb_words=1)
    description = factory.Faker('sentence', nb_words=15)
    price = 0
    customer_price = '00'
