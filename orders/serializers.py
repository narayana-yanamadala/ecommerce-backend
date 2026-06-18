from rest_framework import serializers
from .models import Address, Order, OrderItem


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'full_name', 'phone', 'street', 'landmark',
                  'city', 'state', 'pincode', 'address_type', 'is_default', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_phone(self, value):
        digits = ''.join(filter(str.isdigit, value))
        if len(digits) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 digits.")
        return value

    def validate_pincode(self, value):
        digits = ''.join(filter(str.isdigit, value))
        if len(digits) != 6:
            raise serializers.ValidationError("Pincode must be exactly 6 digits.")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    line_total = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'product_name', 'img_url', 'price', 'quantity', 'line_total']


class OrderSerializer(serializers.ModelSerializer):
    items   = OrderItemSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'address', 'payment_method', 'subtotal', 'discount',
                  'delivery_charge', 'tax', 'total_amount', 'coupon_code',
                  'payment_status', 'order_status', 'razorpay_order_id',
                  'razorpay_payment_id', 'items', 'created_at']
        read_only_fields = ['id', 'created_at']
