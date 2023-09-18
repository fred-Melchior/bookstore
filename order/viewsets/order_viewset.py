from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Funcao que fica na linha de frente da aplicacao
# criando registros com poucas linhas

class OrderViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('id')
