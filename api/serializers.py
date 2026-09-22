from rest_framework import serializers
from .models import User, Category, Product, Order, OrderItem

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role', 'phone')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            role=validated_data.get('role', 'client'),
            phone=validated_data.get('phone', '')
        )
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    vendor_name = serializers.ReadOnlyField(source='vendor.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = (
            'id', 'vendor', 'vendor_name', 'category', 'category_name',
            'title', 'description', 'price', 'stock_quantity', 'unit',
            'image', 'is_available', 'created_at', 'updated_at'
        )
        read_only_fields = ('vendor', 'created_at', 'updated_at')


class OrderItemSerializer(serializers.ModelSerializer):
    product_title = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_title', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    buyer_name = serializers.ReadOnlyField(source='buyer.username')

    class Meta:
        model = Order
        fields = ('id', 'buyer', 'buyer_name', 'total_amount', 'status', 'created_at', 'items')
        read_only_fields = ('buyer', 'total_amount')