from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator
)

from base.models import BaseModel


class Movie(BaseModel):
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    genre = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(4)]
    )
    released = models.IntegerField(validators=[
        MinValueValidator(1940),
        MaxValueValidator(2019)
    ])


class Wine(BaseModel):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)]
    )
    year = models.IntegerField(validators=[
        MinValueValidator(1970),
        MaxValueValidator(2019)
    ])


class Food(BaseModel):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)]
    )
    category = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2)]
    )
    spice_level = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    cost_level = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ])
