from django.db.models import Q
from django.shortcuts import get_object_or_404
from friendship.models import Friendship
from users.models import User
from friendship.api.serializers import FriendshipSerializer


def check_proposition(sender, receiver):
    """ Check if the user did not receive an invitation from the receiver. """
    try:
        proposition = Friendship.objects.get(sender=receiver, receiver=sender)
        return True

    except Friendship.DoesNotExist:
        return False


def list_relationships(user):
    """ Lists friendship requests sent and received from the user. """
    data = {
        'yes': [],
        'no': [],
        'waiting': [],
    }
    relations = Friendship.objects.filter(
        Q(sender=user) | Q(receiver=user)
    )
    for relation in relations:
        if relation.status == 'y':
            data.get('yes').append(FriendshipSerializer(relation).data)
        elif relation.status == 'n':
            data.get('no').append(FriendshipSerializer(relation).data)
        else:
            data.get('waiting').append(FriendshipSerializer(relation).data)

    return data


def check_user(request):
    """ Checks if users exist. """
    sender = get_object_or_404(User,
                               email=request.data.get('sender', None))

    receiver = get_object_or_404(User,
                                 email=request.data.get('receiver', None))

    return sender, receiver
