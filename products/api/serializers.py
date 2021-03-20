from rest_framework import serializers

from products.models import Product, ProductManager


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['product_code', 'created_at', 'creator']
