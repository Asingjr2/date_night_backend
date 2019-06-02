from django.urls import path, include

from content.rest_views import (
    MovieAPIView,
    FoodAPIView,
    WineAPIView
)

urlpatterns = [
    path(
        'movies/',
        MovieAPIView.as_view(),
        name='movie_list'
    ),
    path(
        'foods/',
        FoodAPIView.as_view(),
        name='food_list'
    ),
    path(
        'wines/',
        WineAPIView.as_view(),
        name='wine_list'
    )
]
