from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(
        min_length=2,
        max_length=100
    )
    genre = serializers.CharField(
        min_length=4,
        max_length=50
    )
    released = serializers.IntegerField(
        min_value=1940,
        max_value=2019
    )


class WineSerializer(serializers.Serializer):
    name = serializers.CharField(
        min_length=2,
        max_length=50
    )
    year = serializers.IntegerField(
        min_value=1970,
        max_value=2019
    )


class FoodSerializer(serializers.Serializer):
    name = serializers.CharField(
        min_length=2,
        max_length=50
    )
    category = serializers.CharField(
        min_length=2,
        max_length=50
    )
    spice_level = serializers.IntegerField(
        min_value=1,
        max_value=5
    )
    cost_level = serializers.IntegerField(
        min_value=1,
        max_value=10
    )
