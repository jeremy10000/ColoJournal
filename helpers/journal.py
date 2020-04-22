from journal.api.serializers import JournalSerializer, PageSerializer
from journal.models import Journal, Page
from users.models import User


def list_journals(user):
    """ List journals. """
    data = []
    journals = Journal.objects.filter(user=user)
    for journal in journals:
        data.append(JournalSerializer(journal).data)

    return data


def list_pages(user, journal):
    """ List pages. """
    data = []
    pages = Page.objects.filter(journal=journal)
    for page in pages:
        data.append(PageSerializer(page).data)

    return data
