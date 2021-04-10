from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from User.models import User as UserStatus
from rest_framework import serializers
from .placeorder import PlaceOrder
from django import forms
from .cart import *


User = get_user_model()

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCart
        fields = "__all__"

class PlaceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceOrder
        fields = ["customer", "address", "phone", "total", 'shopId', 'orderedAt']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = UserStatus
        fields = "__all__"
