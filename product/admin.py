from django.contrib import admin
from .models import Brand, Color, CarBody, Car, Image


admin.site.register(Brand)
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(CarBody)
admin.site.register(Car)
