import uuid

from djmoney.models.fields import MoneyField
from django.db.models import *
from django.utils.translation import gettext_lazy as _


class OrderManager(Manager):

    def get_queryset(self):
        return super(OrderManager, self).get_queryset()

    def get_orders(self, customer):
        return self.get_queryset().filter(customer=customer)

    def get_purchase_product(self, customer):
        return self.get_queryset().filter(customer=customer).values_list('product')

    def get_total_revenue(self):
        return self.get_queryset().aggregate(Sum('total'))


class Order(Model):
    order_code = UUIDField(default=uuid.uuid4, editable=False)

    customer = ForeignKey(to='users.Customer', related_name='customer', on_delete=SET_NULL, null=True)

    product = ForeignKey(to='products.Product', related_name='product', on_delete=CASCADE)

    qty = IntegerField(_("quantity"), default=1)

    total = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', default=0)

    created_at = DateField(auto_now_add=True)

    objects = OrderManager()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

        ordering = ("created_at",)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.total += self.product.price * self.qty

        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return '{} [{}]'.format(self.customer, self.total)
