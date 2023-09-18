import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from product.factories import CategoryFactory
from product.models import Category

class TestCategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title='books')

    def test_get_all_categories(self):
        response = self.client.get(
            reverse('category-list')
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)

        self.assertEqual(category_data[0]['title'], self.category.title)

    def test_create_category(self):
        data = json.dumps({
            'title': 'Technology',
            'slug': 'technoly-cat',
        })

        response = self.client.post(
            reverse('category-list'),
            data=data,
            content_type='application/json'
        )

        # import pdb; pdb.set_trace()

        created_category = Category.objects.get(title='Technology')

        self.assertEqual(created_category.title, 'Technology')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
