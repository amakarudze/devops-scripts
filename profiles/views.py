from rest_framework.views import APIView
from rest_framework.response import Response


class UserApiView(APIView):
    """Test API View with User API View"""

    def get(self, request, format=None):
        """Returns a list of APIView"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete).',
            'Is similar to a traditional Django view.',
            'Gives you most control over your application logic.',
            'Is mapped manually to URLs.',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
