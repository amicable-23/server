from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import serializers
from .models import food


# Create your views here.
class foodserializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = "__all__"
        
class foodview(ListCreateAPIView):
    queryset = food.objects.all()
    serializer_class = foodserializer
    
class foodById(RetrieveUpdateDestroyAPIView):
    queryset = food.objects.all()
    serializer_class = foodserializer
    
