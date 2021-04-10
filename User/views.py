from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .serializers import CartSerializer
from .placeorder import PlaceOrder
from User.serializers import *
from Plant.models import Plant
from .cart import CustomerCart


# Create your views here.

@login_required
@api_view(['GET'])
def Home(request):
    context = {
    'Place order' : '/mycart/placedOrder',
    'List of plants' : '/allplants/',
    'Plant detail' : '/plantinfo/',
    'Add to cart' : '/addTocart',
    'My orders' : '/myorders/',
    'My cart' : '/mycart/',
    }
    return Response(context)

@login_required
@api_view(['GET'])
def MyCart(request):
    mycartitems = CustomerCart.objects.filter(customer__id = request.user.id)
    serializer = CartSerializer(mycartitems, many = True)
    return Response(serializer.data)

@login_required
@api_view(['POST'])
def AddToCart(request):
    if request.method == 'POST':
        serializer = CartSerializer(data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@login_required
@api_view(['POST'])
def PlacedOrder(request):
    if request.method == 'POST':
        serializer = PlaceOrderSerializer(data = request.data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@login_required
@api_view(['GET'])
def MyOrders(request):
    myorders = PlaceOrder.objects.filter(customer__customer__id = request.user.id)
    serializer = PlaceOrderSerializer(myorders, many = True)
    return Response(serializer.data)
