from rest_framework import serializers

from friendship.models import Friendship
from users.models import User


class FriendshipSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.email')
    receiver = serializers.CharField(source='receiver.email')
    status = serializers.CharField(min_length=1, max_length=1)

    class Meta:
        model = Friendship
        fields = "__all__"

    def create(self, validated_data):
        """ Create a new instance. """
        sender_email = validated_data['sender'].get('email')
        receiver_email = validated_data['receiver'].get('email')
        sender = User.objects.get(email=sender_email)
        receiver = User.objects.get(email=receiver_email)

        friendship = Friendship(
            sender=sender,
            receiver=receiver,
            status='w'
        )
        friendship.save()

        return friendship

    def update(self, instance, validated_data):
        """ Update a new instance. """
        new_status = validated_data.get('status', None)

        status_accepted = ["y", "n", "w"]

        if new_status not in status_accepted:
            raise ValueError('The status must be y, n or w.')

        friendship = Friendship.objects.filter(id=instance.id).update(
                        status=new_status
                    )
        return friendship
