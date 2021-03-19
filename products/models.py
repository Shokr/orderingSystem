import uuid

from djmoney.models.fields import MoneyField
from django.db.models import *


class ProductManager(Manager):

    def get_queryset(self):
        return super(ProductManager, self).get_queryset()

    def get_products(self, creator):
        return self.get_queryset().filter(creator=creator)


class Product(Model):
    product_code = UUIDField(default=uuid.uuid4, editable=False)

    name = CharField(max_length=250)
    slug = SlugField(max_length=255, unique=True, allow_unicode=True)
    description = TextField(blank=True)

    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    charge_taxes = BooleanField(default=True)

    rating = FloatField(null=True, blank=True)

    creator = ForeignKey(to='users.Admin', related_name='creator', on_delete=SET_NULL, null=True)

    created_at = DateField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True, null=True)

    objects = ProductManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

        ordering = ("slug",)

    def __repr__(self) -> str:
        class_ = type(self)
        return "<%s.%s(pk=%r, name=%r)>" % (
            class_.__module__,
            class_.__name__,
            self.pk,
            self.name,
        )

    def __str__(self) -> str:
        return self.name

    @property
    def plain_text_description(self) -> str:
        return self.description




#     def purchase_product(self, customer, qty):
#         self.qty += qty
#         return self.customers.add(customer)
#
#     def get_purchased_products(self, customer):
#         return self.filter(customers__in=customer)
#
#     def get_total_money_spent(self, customer):
#         return self.filter(customers__in=customer).aggregate(Sum('price'))
#
#     def get_total_revenue(self):
#         total_purchased_products = self.objects.filter(qty__gt=0)
#         pass
# #