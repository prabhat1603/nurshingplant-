
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from User.models import User as userstat
from .serializers import *
from .models import *
# Create your views here.

@login_required
@api_view(['GET'])
def Home(request):
    context = {
    'add plant to my shop' : '/addplanttomyshop',
    'my shop collection' : '/myshopcollection/',
    'create nursery' : '/createnursery/',
    'delete nursery' : '/deleteshop/',
    'all nursery' : '/allnursery/',
    'view nursery' : '/myshop/',
    }
    return Response(context)

@login_required
@api_view(['GET'])
def AllNursery(request):
    nurseries = MyNursery.objects.all()
    serializer = NurserySerializer(nurseries, many = True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def MyShop(request):
    if userstat.objects.get(id=request.user.id).status == "seller":
        myshop = MyNursery.objects.get(seller__id = request.user.id)
        serializer = NurserySerializer(myshop)
        return Response(serializer.data)
    else:
        return Response("Since you are not a seller!")

@login_required
@api_view(['POST'])
def CreateNursery(request):
    if request.method == 'POST' and userstat.objects.get(id=request.user.id).status == "seller":
        serializer = NurserySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response("Since you are not a seller!")

@login_required
@api_view(['POST'])
def UpdateNursery(request, pk):
    instance = MyNursery.objects.get(id = pk)
    if request.method == 'POST' and userstat.objects.get(id=request.user.id).status == "seller":
        serializer = NurserySerializer(data = request.data, instance = instance, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response("Since you are not a seller!")

@login_required
@api_view(['DELETE'])
def DeleteShop(request):
    if userstat.objects.get(id=request.user.id).status == "seller":
        myshop = MyNursery.objects.get(seller__id = request.user.id)
        myshop.delete()
        return Response({'Your shop is deleted!'})
    else:
        return Response("Since you are not a seller!")

@login_required
@api_view(['GET'])
def MyNurseryCollection(request):
    if userstat.objects.get(id=request.user.id).status == "seller":
        collections = NurseryCollection.objects.filter(nursery__id = MyNursery.objects.get(seller__id=request.user.id).id)
        serializer = NurseryCollectionSerializer(collections, many = True)
        return Response(serializer.data)
    else:
        return Response("Since you are not a seller!")

@login_required
@api_view(['POST'])
def AddPlantToMyShop(request):
    if request.method == 'POST' and userstat.objects.get(id=request.user.id).status == "seller":
        serializer = NurseryCollectionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response("Since you are not a seller!")
