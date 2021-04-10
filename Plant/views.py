from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PlantSerializer
from django.contrib import messages
from django.shortcuts import render
from rest_framework import status
from .models import Plant

# Create your views here.

@login_required
@api_view(['GET'])
def Home(request):
    context = {
     'Note' : 'Only admin can add the plant variety',
     'plantdetail' : '/plantdetail/',
     'appendplant' : '/appendplant/',
     'allplants' : '/allplants/'
    }
    return Response(context)

@login_required
@api_view(['GET'])
def AllPlants(request):
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many = True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def PlantDetail(request, pk):
        plant = Plant.objects.get(id = pk)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)

# Only for the admin
# here admin can only add the plant variety
@login_required
@api_view(['POST'])
def AppendPlant(request):
    if request.method == 'POST' and request.user.is_superuser:
        serializer = PlantSerializer(data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response("You can't add the plants as only the admin or superuser can add the new plants!")
