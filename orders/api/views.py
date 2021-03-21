from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import get_object_or_404, CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from products.api.serializers import ProductSerializer
from products.models import Product
from .serializers import Order, OrderSerializer


class PurchasedProductsViewSet(ListAPIView):
    """
    Get_purchased_products:
        allows normal user to retrieve a list of their products
    """

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Product.objects.filter(product__customer_id=request.user.pk)
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class PurchaseProductAPIView(CreateAPIView):
    """
    Purchase_product:
        allows normal users to purchase a product.
    """

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        data = serializer.data

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class GetTotalRevenueAPIView(GenericAPIView):
    """
    Get_total_revenue:
        allows admin users to retrieve the total amount of purchased products.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, ]

    def get(self, request):
        queryset = Order.objects.get_total_revenue()
        return Response(status=status.HTTP_200_OK, data=queryset)
