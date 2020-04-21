from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from friendship.models import Friendship
from helpers.friendship import (check_proposition, check_user,
                                list_relationships)
from users.models import User

from .permissions import IsSenderOrReceiver
from .serializers import FriendshipSerializer


class FriendshipViewSet(viewsets.ModelViewSet):
    """ This viewset manages friendly relationships between users. """

    lookup_field = 'id'
    queryset = Friendship.objects.all()
    permission_classes = (IsAuthenticated, IsSenderOrReceiver)
    serializer_class = FriendshipSerializer

    def list(self, request):
        """ Lists friendship requests sent and received from the user. """

        relations = list_relationships(self.request.user)

        return Response({
            'yes': relations.get('yes'),
            'no': relations.get('no'),
            'waiting': relations.get('waiting')
            }, status=status.HTTP_200_OK)

    def retrieve(self, request, id=None):
        """ Retrieves information from a friendship relationship. """
        relation = get_object_or_404(self.queryset, id=id)
        self.check_object_permissions(request, relation)
        serializer = FriendshipSerializer(relation)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """ Create a friendly relationship between two users."""

        # Check if users exist.
        sender, receiver = check_user(request)

        if self.request.user != sender:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # Checks if the user did not receive an invitation
        proposition = check_proposition(sender, receiver)
        if proposition:
            return Response(status=status.HTTP_302_FOUND)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """ Put request """
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def partial_update(self, request, *args, **kwargs):
        """
        Patch request. Only the person who received the friendship request
        can change the relationship.

        """
        instance = self.get_object()

        if self.request.user != instance.receiver:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, id=None):
        """ Only the persons concerned can delete a relationship. """
        relation = get_object_or_404(self.queryset, id=id)
        self.check_object_permissions(request, relation)
        self.perform_destroy(relation)

        return Response(status=status.HTTP_204_NO_CONTENT)
