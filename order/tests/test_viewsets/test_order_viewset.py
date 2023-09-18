import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory, OrderFactory

from product.models import Product
from order.models import Order

class TestOrderViewSet(APITestCase):

    client = APIClient()

#       ESTRURA INICIAL DO TESTE:

    def setUp(self):
        self.category = CategoryFactory(title='Technology')
        self.product = ProductFactory(title='Mouse', price=100, category=[self.category])
        self.order = OrderFactory(product=[self.product])

#       Testa a funcionalidade order atraves do GET

    def test_order(self):
        response = self.client.get(
            reverse('order-list')
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)
        self.assertEqual(order_data['results'][0]['product'][0]['title'], self.product.title)
        self.assertEqual(order_data['results'][0]['product'][0]['price'], self.product.price)
        self.assertEqual(order_data['results'][0]['product'][0]['active'], self.product.active)
        self.assertEqual(order_data['results'][0]['product'][0]['category'][0]['title'], self.category.title)

#       Testa a funcionalidade de criar uma order atraves do POST

    def test_create_order(self):
        user = UserFactory()
        product = ProductFactory()
        data = json.dumps({
            'products_id': [product.id],
            'user': user.id
        })

        # import pdb; pdb.set_trace()

        response = self.client.post(
            reverse('order-list', current_app='order'),
            data=data,
            content_type='application/json'
        )

        created_order = Order.objects.get(user=user)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(created_order['product']['id'], self.product.id)