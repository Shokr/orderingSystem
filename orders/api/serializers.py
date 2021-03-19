from rest_framework import serializers

from orders.models import Order, OrderManager

# from users.api.serializers import CustomerSerializer
# from products.api.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer(read_only=True)
    # product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_code', 'created_at', 'total']
