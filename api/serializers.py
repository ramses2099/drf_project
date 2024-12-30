from rest_framework import serializers

from .models import Order, OrderItem, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price','stock',]
    
    def validate_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('Stock cannot be negative.')
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']           


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total',read_only=True)

    def total(self, obj):
        order_items = obj.items.all()
        return sum([item.item_subtotal for item in order_items])

    class Meta:
        model = Order
        fields = ['order_id', 'create_at', 'user','status', 'items', 'total_price']

# Custom Serializar
class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()