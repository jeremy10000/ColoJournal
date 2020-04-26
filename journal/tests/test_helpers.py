from rest_framework.test import APITestCase

from users.models import User
from journal.models import Journal

from helpers.journal import *


class HelpersJournalTestCase(APITestCase):
    """ Helper journals """
    fixtures = ["journal.json"]

    def test_check_shared_journals(self):
        user = User.objects.get(id=1)
        data = check_shared_journals(user)
        expected = [{
            'id': 5, 'name': 'Afrique du Sud',
            'date': '2020-01-20', 'shared': True
        }]
        self.assertEqual(data, expected)

    def test_check_shared_pages(self):
        user = User.objects.get(id=1)
        data = check_shared_pages(user, 5)
        expected = [{
            'id': 4, 'name': 'Jour 1 en ADS', 'text': 'Nous avons...',
            'journal': 5, 'journal_name': 'Afrique du Sud'
        }]
        self.assertEqual(data, expected)

        # <QuerySet []>
        data = check_shared_pages(user, 1)
        self.assertFalse(data)
