from rest_framework import permissions, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

from .serializers import Product, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
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

    queryset = Product.objects.get_queryset()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]
