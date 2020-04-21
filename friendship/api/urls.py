from django.urls import path, include
from rest_framework import routers

from .views import FriendshipViewSet


router = routers.SimpleRouter()
router.register(r'friendship', FriendshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
