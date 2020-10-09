from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles import serializers


class UserApiView(APIView):
    """Test API View with User API View"""
    serializers_class = serializers.UserSerializer

    def get(self, request, format=None):
        """Returns a list of APIView"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete).',
            'Is similar to a traditional Django view.',
            'Gives you most control over your application logic.',
            'Is mapped manually to URLs.',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a message with our username"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name')
            message = f'Hello {first_name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object."""

