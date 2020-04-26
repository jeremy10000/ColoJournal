from rest_framework.test import APITestCase

from users.models import User
from journal.models import Journal

from helpers.friendship import *


class HelpersFriendshipTestCase(APITestCase):
    """ Helper friendship """
    fixtures = ["viewset.json"]

    def setUp(self):
        self.user = User.objects.get(id=1)
        self.friend = User.objects.get(id=2)

    def test_check_friend(self):
        not_friend = User.objects.get(id=5)

        # yes
        data = check_friend(self.user, self.friend)
        self.assertTrue(data)

        # no
        data = check_friend(self.user, not_friend)
        self.assertFalse(data)

    def test_check_proposition(self):
        data = check_proposition(self.friend, self.user)
        self.assertTrue(data)
