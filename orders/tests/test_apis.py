from rest_framework import status
from rest_framework.test import APITransactionTestCase

from users.tests.factories import UserFactory
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class TestThis(APITransactionTestCase):
    def setUp(self):
        self.user = UserFactory.create()
        token = Token.objects.get_or_create(user=self.user)
        self.client = APIClient(HTTP_AUTHORIZATION='Token ' + token[0].key)

    def test_api_can_get_purchased_products(self):
        response = self.client.get(path='/api/get_purchased_products', format='json')
        if response.status_code == status.HTTP_200_OK:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_api_can_get_total_revenue(self):
        response = self.client.get(path='/api/get_total_revenue', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'total__sum')
