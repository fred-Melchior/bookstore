from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer


# Funcao que fica na linha de frente da aplicacao
# criando registros com poucas linhas

class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('id')
