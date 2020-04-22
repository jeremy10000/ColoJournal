from django.urls import path, include
from rest_framework import routers

from .views import JournalViewSet, PageViewSet


router = routers.SimpleRouter()
router.register(r'journals', JournalViewSet)
router.register(r'pages', PageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
