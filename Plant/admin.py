from django.contrib import admin
from .models import Plant

# Register your models here.

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "cost"]
