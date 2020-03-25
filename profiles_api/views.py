from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Reruns a list of APIView features"""
        an_apiview = [
            'Uses HTPP methos as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your applcation logic',
            'is mapped manually to URLs'
        ]

        return Response({'message' : 'hello', 'an_apiView': an_apiview})
