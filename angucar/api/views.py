from rest_framework import viewsets
from cars.models import CarModel
from cars.serializers import CarModelSerializer
from rest_framework import mixins
from orders.models import Order
from orders.serializers import OrderSerializer


class CarModelVS(viewsets.ReadOnlyModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class ModelViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.object.all()
    serializer_class = OrderSerializer