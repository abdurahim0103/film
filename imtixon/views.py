from django.shortcuts import render
from .models import Film, Actor, Category, Info
from .serializer import FilmSerializer, ActorSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class FilmViewset(ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()

class ActorViewset(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

class GetCategory(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many= True)







