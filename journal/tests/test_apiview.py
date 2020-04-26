from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.models import User
from journal.models import Journal


class APIViewTestCase(APITestCase):
    """ Tests APIView """
    fixtures = ["viewset.json"]

    def setUp(self):
        self.user = User.objects.get(id=1)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_list_not_found(self):
        response = self.client.get("/api/friend/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_ok_is_my_friend(self):
        response = self.client.get("/api/friend/?id=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_forbidden(self):
        response = self.client.get("/api/friend/?id=5")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
