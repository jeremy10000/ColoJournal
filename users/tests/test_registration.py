from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):
    """ Registration tests """

    def test_registration_successful(self):
        data = {'email': 'test@test.fr', 'password': 'france2020'}
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_failed(self):
        """
        The password is too short.
        The email address is invalid.
        """
        data = {'email': 'test@test.fr', 'password': 'france'}
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {'email': 'test.fr', 'password': 'france2020'}
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
