from django.shortcuts import render
from apiApp.serializers import CourseSerializer
from rest_framework import viewsets
from apiApp.models import Course

# Create your views here.

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all() #queryset is default name do not change it
    serializer_class = CourseSerializer
