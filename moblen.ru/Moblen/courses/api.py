from django.shortcuts import render
from rest_framework import viewsets
from .models import Course, Topic, Task, TaskList
from .serializers import CourseSerializer, TopicSerializer, TaskSerializer, TaskListSerializer


class CourseAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or created by tutor UUID.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'owner_uuid'

    def create(self, request, owner_uuid=None):



class CourseTutorAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific course to be retrieved, updated, or deleted.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'owner_uuid'


