from django.contrib import admin
from .models import Brand, Color, CarBody, Car, Image, Basket


class CarAdmin(admin.ModelAdmin):
    list_display = ('user', 'car_model', 'created_date', 'status')
    prepopulated_fields = {"slug": ("car_model", )}


admin.site.register(Brand)
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(CarBody)
admin.site.register(Car, CarAdmin)
admin.site.register(Basket)
