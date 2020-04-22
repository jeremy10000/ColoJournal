from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from helpers.journal import list_journals, list_pages
from journal.models import Journal, Page
from users.models import User

from .permissions import IsAuthor
from .serializers import JournalSerializer, PageSerializer


class JournalViewSet(viewsets.ModelViewSet):
    """ This viewset manages users journals. """

    lookup_field = 'id'
    queryset = Journal.objects.all()
    permission_classes = (IsAuthenticated, IsAuthor)
    serializer_class = JournalSerializer

    def list(self, request):
        """ List user journals. """
        journals = list_journals(self.request.user)

        return Response(journals, status=status.HTTP_200_OK)

    def retrieve(self, request, id=None):
        """ Retrieve a journal. """

        journal = get_object_or_404(self.queryset, id=id)
        self.check_object_permissions(request, journal)
        serializer = JournalSerializer(journal)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """ Create a journal."""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """ Put request """
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def partial_update(self, request, *args, **kwargs):
        """ Patch request. Update a journal. """
        instance = self.get_object()

        self.check_object_permissions(request, instance)

        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, id=None):
        """ Delete a journal. """
        journal = get_object_or_404(self.queryset, id=id)
        self.check_object_permissions(request, journal)
        self.perform_destroy(journal)

        return Response(status=status.HTTP_204_NO_CONTENT)


class PageViewSet(viewsets.ModelViewSet):
    """ This viewset manages users pages. """

    lookup_field = 'id'
    queryset = Page.objects.all()
    permission_classes = (IsAuthenticated, IsAuthor)
    serializer_class = PageSerializer

    def list(self, request):
        """ List the pages of a journal. """

        journal = request.data.get('journal', None)
        if journal is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        journal = get_object_or_404(Journal.objects.all(), id=journal)
        self.check_object_permissions(request, journal)
        pages = list_pages(self.request.user, journal)

        return Response(pages, status=status.HTTP_200_OK)

    def retrieve(self, request, id=None):
        """ Retrieve a page from a journal. """

        page = get_object_or_404(self.queryset, id=id)
        self.check_object_permissions(request, page.journal)
        serializer = PageSerializer(page)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """ Create a page."""

        journal = request.data.get('journal', None)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user, journal=journal)

        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """ Put request """
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def partial_update(self, request, *args, **kwargs):
        """ Patch request. Update a page. """
        instance = self.get_object()

        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, id=None):
        """ Delete a page. """
        page = get_object_or_404(self.queryset, id=id)
        self.check_object_permissions(request, page)
        self.perform_destroy(page)

        return Response(status=status.HTTP_204_NO_CONTENT)
