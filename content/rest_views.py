from rest_framework.views import APIView
from rest_framework.response import Response


class MovieAPIView(APIView):
    def get(self, request):
        data = {
            'message': 'Movie page'
        }

        return Response(data)


class FoodAPIView(APIView):
    def get(self, request):
        data = {
            'message': 'Food page'
        }
        
        return Response(data)


class WineAPIView(APIView):
    def get(self, request):
        data = {
            'message': 'Wine page'
        }
        
        return Response(data)
