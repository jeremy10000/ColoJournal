from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from helpers.journal import list_journals, list_pages, check_shared_journals, check_shared_pages
from helpers.friendship import check_friend
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

        # journal = request.data.get('journal', None)
        journal = request.query_params.get('journal', None)
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


class JournalListAPIView(generics.ListAPIView):
    """ List journals for friends """
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def list(self, request):
        user = request.query_params.get('id', None)
        user = get_object_or_404(User.objects.all(), id=user)
        # a friend ?
        is_friend = check_friend(self.request.user, user)
        if is_friend is False:
            return Response(status=status.HTTP_403_FORBIDDEN)

        shared_journals = check_shared_journals(user)

        return Response(shared_journals, status.HTTP_200_OK)


class PageListAPIView(generics.ListAPIView):
    """ List journals for friends """
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def list(self, request):
        print('request.query_params', request.query_params)
        journal = request.query_params.get('id', None)
        journal = get_object_or_404(Journal.objects.all(), id=journal)
        print('journal demandé', journal.name, 'id:', journal.id, 'user:', journal.user)
        print('self.request.user:', self.request.user, 'id:', self.request.user.id)
        # vérifie si l'user demandé est l'ami de celui qui demande...
        is_friend = check_friend(self.request.user, journal.user)
        # pas ami
        if is_friend is False:
            print("Pas ami, pas de pages !")
            return Response(status=status.HTTP_403_FORBIDDEN)
        # c'est un ami, on regarde si l'user demandé à des journaux partagés
        print("OUI")
        shared_pages = check_shared_pages(journal.user, journal.id)
        if shared_pages is False:
            print("Journal pas partagé, pas de pages !")
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        
        return Response(shared_pages, status.HTTP_200_OK)
