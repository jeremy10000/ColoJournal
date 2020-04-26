from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework.authtoken.models import Token
from users.models import User


class LoginTestCase(APITestCase):
    """ Login tests """

    def setUp(self):
        self.user = User.objects.create_user(email="amazing@test.fr",
                                             password="password2020")
        self.token = Token.objects.create(user=self.user)

    def test_login(self):
        data = {'username': 'amazing@test.fr', 'password': 'password2020'}
        response = self.client.post("/api/login/", data)
        self.assertEqual(response.data.get('token'), self.token.key)
        self.assertEqual(response.data.get('user'), 'amazing@test.fr')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_error(self):
        data = {'username': 'amazing@test.fr', 'password': 'pass'}
        response = self.client.post("/api/login/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
