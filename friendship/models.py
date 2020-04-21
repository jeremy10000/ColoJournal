from django.db import models
from users.models import User


class Friendship(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="senders")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="receivers")
    # y = yes, n = no, w = waiting
    status = models.CharField(default="w", max_length=1)

    def __str__(self):
        return str(self.sender.email) + " - " + str(self.receiver.email)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['sender', 'receiver'],
                name='friendship_unique')
        ]
