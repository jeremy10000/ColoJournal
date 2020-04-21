from django.contrib import admin
from friendship.models import Friendship


class FriendshipAdmin(admin.ModelAdmin):

    list_display = ("id", "sender", "receiver", "status")


admin.site.register(Friendship, FriendshipAdmin)
