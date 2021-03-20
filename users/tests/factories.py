import factory
from django.contrib.auth.hashers import make_password
from django.utils.text import slugify

from users.models import User, Admin, Customer


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttribute(lambda o: slugify(o.first_name + '.' + o.last_name))
    email = factory.LazyAttribute(lambda a: '{0}.{1}@example.com'.format(a.first_name, a.last_name).lower())
    password = factory.LazyFunction(lambda: make_password('pi3.1415'))
    is_staff = True
    is_superuser = True


class AdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Admin

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttribute(lambda o: slugify(o.first_name + '.' + o.last_name))
    email = factory.LazyAttribute(lambda a: '{0}.{1}@example.com'.format(a.first_name, a.last_name).lower())
    password = factory.LazyFunction(lambda: make_password('pi3.1415'))
    type = "ADMIN"
    is_staff = True
    is_superuser = True


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttribute(lambda o: slugify(o.first_name + '.' + o.last_name))
    email = factory.LazyAttribute(lambda a: '{0}.{1}@example.com'.format(a.first_name, a.last_name).lower())
    password = factory.LazyFunction(lambda: make_password('pi3.1415'))
    type = "CUSTOMER"
    is_staff = False
    is_superuser = False
