from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.models import User
from friendship.models import Friendship


class FriendshipViewSetTestCase(APITestCase):
    """
    Tests viewset methods: create(), list(), retrieve(),
    update(), partial_update() and destroy()

    """
    fixtures = ["viewset.json"]

    def setUp(self):
        self.user = User.objects.get(id=3)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_list_anonymous_user(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/friendship/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_authenticated(self):
        response = self.client.get("/api/friendship/")
        self.assertEqual(len(response.data.get('yes')), 1)
        self.assertEqual(len(response.data.get('no')), 0)
        self.assertEqual(len(response.data.get('waiting')), 0)
        self.assertEqual(len(response.data.get('received')), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_is_sender_or_receiver(self):
        response = self.client.get("/api/friendship/2/")
        self.assertEqual(response.data.get('sender'), "avril@mail.fr")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_is_not_sender_or_receiver(self):
        response = self.client.get("/api/friendship/1/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_authenticated(self):
        data = {"sender": "avril@mail.fr", "receiver": "decembre@mail.fr",
                "status": "w"}
        response = self.client.post("/api/friendship/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_anonymous_user(self):
        self.client.force_authenticate(user=None)
        data = {"sender": "avril@mail.fr", "receiver": "decembre@mail.fr",
                "status": "w"}
        response = self.client.post("/api/friendship/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_not_exists(self):
        data = {"sender": "avril@mail.fr", "receiver": "jesus@mail.fr",
                "status": "w"}
        response = self.client.post("/api/friendship/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_user_authenticated_is_not_sender(self):
        data = {"sender": "python@mail.fr", "receiver": "decembre@mail.fr",
                "status": "w"}
        response = self.client.post("/api/friendship/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_destroy_user_is_sender_or_receiver(self):
        response = self.client.delete("/api/friendship/2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_destroy_user_is_not_sender_or_receiver(self):
        response = self.client.delete("/api/friendship/1/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_destroy_not_found(self):
        response = self.client.delete("/api/friendship/90/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_user_is_sender_unauthorized(self):
        """ Only the person who received the request can update. """
        data = {"sender": "avril@mail.fr", "receiver": "django@mail.fr",
                "status": "w"}
        response = self.client.patch("/api/friendship/2/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_user_is_not_sender_or_receiver(self):
        data = {"sender": "avril@mail.fr", "receiver": "django@mail.fr",
                "status": "w"}
        response = self.client.patch("/api/friendship/1/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user_is_receiver(self):
        response = self.client.get("/api/friendship/3/")
        self.assertEqual(response.data.get('status'), 'w')

        data = {"sender": "ville@mail.fr", "receiver": "avril@mail.fr",
                "status": "y"}
        response = self.client.patch("/api/friendship/3/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get("/api/friendship/3/")
        self.assertEqual(response.data.get('status'), 'y')

    def test_update_not_found(self):
        data = {}
        response = self.client.patch("/api/friendship/300/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_bad_status(self):
        data = {"sender": "ville@mail.fr", "receiver": "avril@mail.fr",
                "status": "a"}
        with self.assertRaises(ValueError):
            response = self.client.patch("/api/friendship/3/", data)

    def test_update_put_method_unauthorized(self):
        data = {"sender": "avril@mail.fr", "receiver": "django@mail.fr",
                "status": "w"}
        response = self.client.put("/api/friendship/2/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
