from django.contrib import admin

from .models import (
    Movie,
    Wine,
    Food
)

# Register your models here.
admin.site.register(Movie)
admin.site.register(Wine)
admin.site.register(Food)
