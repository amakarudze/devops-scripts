from rest_framework.serializers import Serializer, CharField


class UserSerializer(Serializer):
    """Serializes a name field for testing our APIView"""
    first_name = CharField(max_length=100)
