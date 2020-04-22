from rest_framework.permissions import BasePermission
from journal.models import Page


class IsAuthor(BasePermission):
    """ Check if the user is the author. """

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Page):
            return request.user == obj.journal.user

        return request.user == obj.user
