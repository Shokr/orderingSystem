from rest_framework import permissions, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.response import Response

from .serializers import Product, ProductSerializer

from users.models import User

from djmoney.money import Money
from djmoney.contrib.exchange.models import convert_money


class ProductViewSet(viewsets.ModelViewSet):
    """
    ProductViewSet:
        Admin Api to deal with products.

        retrieve:
        Allows admin user to retrieve the given Product.

        list:
        Allows admin user to retrieve a list of all Products that exist

        create:
        Allows admin user to create a Product to a normal user

        update:
        Allows admin user to modify a Product that already exists

        destroy:
        Allows admin user to delete a Product that already exists
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, ]

    def perform_create(self, serializer):
        """
        Overwite create() method to allow to add creator user.
        :param serializer:
        :return: Create a new Product.
        """
        serializer.save(creator=self.request.user)


class AllProductsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    AllProductsViewSet:
        Customer Api to deal with products.

        retrieve:
            Allows user to retrieve the given Product.

        list:
            Allows user to retrieve a list of all Products that exist
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]

    serializer_class = ProductSerializer

    # queryset = Product.objects.get_queryset()

    # user currency might be different from product currency so converte to his currency.
    def get_queryset(self):
        user_currency = User.objects.filter(pk=self.request.user.id).values_list('currency')
        user_currency = user_currency[0][0]
        print(user_currency)

        queryset = Product.objects.get_queryset()

        for product in queryset:
            pk = product.pk
            price = product.price
            print(pk, price)

            converted_price = str(convert_money(price, user_currency))
            print(converted_price)

            Product.objects.filter(pk=pk).update(customer_price=converted_price)

        return queryset
