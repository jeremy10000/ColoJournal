from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from journal.models import Page
from users.models import User


class PageViewSetTestCase(APITestCase):
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
        response = self.client.get("/api/pages/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.get("/api/pages/?journal=1")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_authenticated(self):
        response = self.client.get("/api/pages/?journal=1")
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_is_author(self):
        response = self.client.get("/api/pages/1/")
        self.assertEqual(response.data.get('name'), "Premier jour")
        self.assertEqual(response.data.get('text'), "Ce samedi on a...")
        self.assertEqual(response.data.get('journal'), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_is_not_my_journal(self):
        response = self.client.get("/api/pages/3/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_not_found(self):
        response = self.client.get("/api/pages/400/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_authenticated(self):
        data = {"name": "Week-end", "text": "Il a fait beau!", "journal": 1}
        response = self.client.post("/api/pages/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_anonymous_user(self):
        self.client.force_authenticate(user=None)
        data = {"name": "Week-end", "text": "Il a fait beau!"}
        response = self.client.post("/api/pages/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_serializer_invalid(self):
        data = {"text": "Il a fait beau!"}
        response = self.client.post("/api/pages/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {"name": "Week-end"}
        response = self.client.post("/api/pages/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_destroy_is_author(self):
        response = self.client.delete("/api/pages/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_destroy_is_not_my_journal(self):
        response = self.client.delete("/api/pages/3/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_is_not_author(self):
        data = {"name": "Week-end", "text": "Il a fait beau!"}
        response = self.client.patch("/api/pages/3/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_is_author(self):
        data = {"name": "Week-end", "text": "Il a fait beau!", "journal": 1}
        self.client.patch("/api/pages/1/", data)

        response = self.client.get("/api/pages/1/")
        self.assertEqual(response.data.get('name'), "Week-end")
        self.assertEqual(response.data.get('text'), "Il a fait beau!")
        self.assertEqual(response.data.get('journal'), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_not_found(self):
        data = {"name": "Week-end", "text": "Il a fait beau!"}
        response = self.client.patch("/api/pages/400/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_invalid(self):
        data = {"name": "Week-end"}
        response = self.client.patch("/api/pages/1/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_put_method_unauthorized(self):
        data = {"name": "Week-end", "text": "Il a fait beau!"}
        response = self.client.put("/api/pages/1/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
