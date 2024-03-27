from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializer import *
from rest_framework.response import Response


class ClientView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get', 'post']


class ProductView(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PaymentView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['get', 'post']

    def retrieve(self, request, pk):
        payment = Payment.objects.filter(client_id=pk)
        serialized_data = PaymentSerializer(payment, many=True).data
        return Response(serialized_data)


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post']

    def retrieve(self, request, pk):
        order = Order.objects.filter(client_id=pk)
        serialized_data = OrderSerializer(order, many=True).data
        return Response(serialized_data)


class OrderItemView(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    http_method_names = ['get', 'post']
