from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order;
        fields = [
            'id',
            'engine',
            'wheels',
            'exterior_color',
            'interior',
            'autopilot',
            'firstname',
            'lastname',
            'phone',
            'email',
            'card_number',
            'card_date',
        ];