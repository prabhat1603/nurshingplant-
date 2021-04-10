from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(MyNursery)
class MyNurseryAdmin(admin.ModelAdmin):
    list_display = ["id", "shopName", "contact"]


@admin.register(NurseryCollection)
class NurseryCollectionAdmin(admin.ModelAdmin):
    list_display = ["id", "plant", "nursery"]
