from django.contrib import admin
from .models import CarModel

class CarAdmin(admin.ModelAdmin):
    admin.site.register(CarModel)
