from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


from .models import (
    Movie, 
    Food,
    Wine
)

from .seriliazers import (
    MovieSerializer,
    FoodSerializer,
    WineSerializer
)


class MovieAPIView(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)


class FoodAPIView(APIView):
    def get(self, request, format=None):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)

        return Response(serializer.data)


class WineAPIView(APIView):
    def get(self, request, format=None):
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)

        return Response(serializer.data)
