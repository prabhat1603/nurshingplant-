from rest_framework import serializers
from .models import *

class NurserySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyNursery
        fields = "__all__"

class NurseryCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseryCollection
        fields = "__all__"
