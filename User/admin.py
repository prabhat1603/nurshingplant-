from .placeorder import PlaceOrder
from django.contrib import admin
from .cart import CustomerCart
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "status", "phone"]

@admin.register(CustomerCart)
class CustomerCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'shopFrom','plant', 'quantity']

@admin.register(PlaceOrder)
class PlaceOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'address', 'phone']
