from dataclasses import field
from rest_framework import serializers
from apiApp.models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'url', 'language', 'price')
