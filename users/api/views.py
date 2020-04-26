from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class RegistrationAPIView(APIView):
    """ Registration endpoints """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # If invalid, return 400 Bad Request.
        serializer.is_valid(raise_exception=True)
        # Calls the create method of the serializer.
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ObtainAuthTokenUser(ObtainAuthToken):
    """ Return Token and Username """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': serializer.data.get('username')})
