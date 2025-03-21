from django.shortcuts import render
from rest_framework import viewsets
from .models import Homework
from .serializer import HomeworkSerializer

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
