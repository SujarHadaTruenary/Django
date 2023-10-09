from django.shortcuts import render
from rest_framework import viewsets
from .models import todo
from .serializers import *
from django.core import serializers
import requests

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer


