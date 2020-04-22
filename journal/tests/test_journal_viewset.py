from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.models import User
from journal.models import Journal


class JournalViewSetTestCase(APITestCase):
    """
    Tests viewset methods: create(), list(), retrieve(),
    update(), partial_update() and destroy()

    """
    fixtures = ["journal.json"]

    def setUp(self):
        self.user = User.objects.get(id=1)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_list_anonymous_user(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/journals/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_authenticated(self):
        response = self.client.get("/api/journals/")
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_is_author(self):
        response = self.client.get("/api/journals/1/")
        self.assertEqual(response.data.get('name'), "Thailande")
        self.assertEqual(response.data.get('shared'), False)
        self.assertEqual(response.data.get('date'), "2020-01-20")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_is_not_author(self):
        response = self.client.get("/api/journals/4/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_not_found(self):
        response = self.client.get("/api/journals/400/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_authenticated(self):
        data = {"name": "Canada", "date": "2018-10-11"}
        response = self.client.post("/api/journals/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_anonymous_user(self):
        self.client.force_authenticate(user=None)
        data = {"name": "Canada", "date": "2018-10-11"}
        response = self.client.post("/api/journals/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_serializer_invalid_date(self):
        data = {"name": "Canada", "date": "2018"}
        response = self.client.post("/api/journals/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_destroy_is_author(self):
        response = self.client.delete("/api/journals/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_destroy_is_not_author(self):
        response = self.client.delete("/api/journals/4/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_is_not_author(self):
        data = {"name": "Canada", "date": "2018-10-11", 'shared': True}
        response = self.client.patch("/api/journals/4/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_is_author(self):
        data = {"name": "Suède", "date": "2015-06-01", 'shared': True}

        response = self.client.get("/api/journals/1/")
        self.assertEqual(response.data.get('name'), "Thailande")
        self.assertEqual(response.data.get('shared'), False)

        self.client.patch("/api/journals/1/", data)

        response = self.client.get("/api/journals/1/")
        self.assertEqual(response.data.get('name'), "Suède")
        self.assertEqual(response.data.get('shared'), True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_not_found(self):
        data = {"name": "Canada", "date": "2018-10-11", 'shared': True}
        response = self.client.patch("/api/journals/400/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid(self):
        data = {"date": "2018-10-11", 'shared': True}
        response = self.client.patch("/api/journals/1/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_put_method_unauthorized(self):
        data = {"date": "2018-10-11", 'shared': True}
        response = self.client.put("/api/journals/1/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
