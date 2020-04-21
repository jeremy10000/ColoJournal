from rest_framework.permissions import BasePermission


class IsSenderOrReceiver(BasePermission):
    """ Check if the user is the sender or the receiver. """

    def has_object_permission(self, request, view, obj):
        if request.user == obj.receiver or request.user == obj.sender:
            return True

        return False
