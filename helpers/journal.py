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


def check_shared_journals(friend):
    """ Lists the shared journals. """
    data = []
    journals = Journal.objects.filter(user=friend, shared=True)
    for journal in journals:
        data.append(JournalSerializer(journal).data)

    return data


def check_shared_pages(friend, journal_id):
    """ Returns the pages of the shared journals. """
    data = []
    try:
        journal = Journal.objects.filter(
            id=journal_id,
            user=friend,
            shared=True
        )
        # if journal <QuerySet []>
        if not journal:
            return False

        pages = Page.objects.filter(journal=journal_id)
        for page in pages:
            data.append(PageSerializer(page).data)

        return data

    except Journal.DoesNotExist:
        return False
