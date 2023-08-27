from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from random_array_app.views import RandomArrayView

class RandomArrayViewTests(APITestCase):

    def setUp(self):
        self.url = reverse("random_array")
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

   
    def test_missing_sentence_parameter(self):
        response = self.client.post(self.url, {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_invalid_sentence_type(self):
        data = {"sentence": 123}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_server_error(self):
        with patch.object(RandomArrayView, "generate_random_floats", side_effect=Exception("Test exception")):
            data = {"sentence": "test sentence"}
            response = self.client.post(self.url, data, format="json")

            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertIn("error", response.data)



