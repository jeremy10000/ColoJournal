"""colojournal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from rest_framework.authtoken.views import ObtainAuthToken
from users.api.views import ObtainAuthTokenUser
from journal.api.views import JournalListAPIView, PageListAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', ObtainAuthTokenUser.as_view()),
    path('api/', include('users.api.urls')),
    path('api/', include('friendship.api.urls')),
    path('api/', include('journal.api.urls')),
    path('api/friend/', JournalListAPIView.as_view()),
    path('api/friend/pages/', PageListAPIView.as_view())
]
