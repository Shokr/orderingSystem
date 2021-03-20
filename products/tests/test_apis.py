import json
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from users.tests.factories import UserFactory
from products.models import Product
from products.tests.factories import ProductFactory


class TestProductAPIs(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        token = Token.objects.get_or_create(user=self.user)
        self.client = APIClient(HTTP_AUTHORIZATION='Token ' + token[0].key)

    def test_create_product(self):
        data = {
            "name": "Hitech",
            "slug": "HT",
            "description": "hello man",
            "price": "100",
            "customer_price": "0",
            "charge_taxes": True,
            "rating": 0
        }
        response = self.client.post('/api/products/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = response.json()
        self.assertEqual(response['name'], data['name'])
        self.assertEqual(response['description'], data['description'])
        self.assertEqual(response['slug'], data['slug'])

    def test_create_product_missing_data(self):
        data = {
            'description': 'test description'
        }
        response = self.client.post('/api/products/', data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        response = response.json()
        self.assertEqual(response['name'], ['This field is required.'])
        self.assertEqual(response['slug'], ['This field is required.'])
        self.assertEqual(response['price'], ['This field is required.'])

    def test_update_product(self):
        data = {
            "name": "Himedia",
            "slug": "HM",
            "description": "hello man",
            "price": "100",
            "customer_price": "0",
            "charge_taxes": True,
            "rating": 0
        }
        product = ProductFactory.create(slug="HT")
        response = self.client.put('/api/products/{}/'.format(product.pk),
                                   data=json.dumps(data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        product.refresh_from_db()
        self.assertEqual(response['name'], data['name'])
        self.assertEqual(response['description'], data['description'])
        self.assertEqual(response['charge_taxes'], True)

    def test_parital_update_product(self):
        data = {
            'description': 'test description'
        }
        product = ProductFactory.create(charge_taxes=False)
        response = self.client.patch(
            '/api/products/{}/'.format(product.pk),
            data=json.dumps(data),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = response.json()
        product.refresh_from_db()
        self.assertEqual(response['description'], data['description'])
        self.assertEqual(response['charge_taxes'], False)

    def test_delete_product(self):
        product = ProductFactory.create(slug='LOVE')
        response = self.client.delete('/api/products/{}/'.format(product.pk), content_type='application/json')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Product.objects.filter(pk=product.pk).exists())
