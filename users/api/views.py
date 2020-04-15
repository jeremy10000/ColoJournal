from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer


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
