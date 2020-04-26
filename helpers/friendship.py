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
        # My friends
        'yes': [],
        # Not friends.
        'no': [],
        # Request sent - waiting for a response
        'waiting': [],
        # Request received - Need Answer.
        'received': [],
    }
    relations = Friendship.objects.filter(
        Q(sender=user) | Q(receiver=user)
    )

    for relation in relations:
        # Requests received.
        if relation.receiver == user:
            change = FriendshipSerializer(relation).data
            change['user_id'] = int(relation.sender.id)
            change['mail'] = str(relation.sender)
            change.pop('receiver')
            change.pop('sender')
            if relation.status == 'w':
                data.get('received').append(change)
            elif relation.status == 'n':
                data.get('no').append(change)
            else:
                data.get('yes').append(change)

        # Requests sent
        if relation.sender == user:
            change = FriendshipSerializer(relation).data
            change['user_id'] = int(relation.receiver.id)
            change['mail'] = str(relation.receiver)
            change.pop('receiver')
            change.pop('sender')

            if relation.status == 'w':
                data.get('waiting').append(change)
            elif relation.status == 'n':
                data.get('no').append(change)
            else:
                data.get('yes').append(change)

    return data


def check_user(request):
    """ Checks if users exist. """
    sender = get_object_or_404(User,
                               email=request.data.get('sender', None))

    receiver = get_object_or_404(User,
                                 email=request.data.get('receiver', None))

    return sender, receiver


def check_friend(request_user, friend):
    """ Check if he's a friend. """
    try:
        relation = Friendship.objects.get(
            Q(sender=request_user, receiver=friend, status='y') |
            Q(sender=friend, receiver=request_user, status='y')
        )
        return True

    except Friendship.DoesNotExist:
        return False
