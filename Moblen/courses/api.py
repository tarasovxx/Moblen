from django.shortcuts import render
from rest_framework import viewsets
from .models import Course, Topic, Task, TaskList
from .serializers import CourseSerializer, TopicSerializer, TaskSerializer, TaskListSerializer


class CourseAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or created.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseTutorAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific course to be retrieved, updated, or deleted.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'owner_uuid'


class CourseDetailAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific course to be retrieved, updated, or deleted.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'course_uuid'


class TopicAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows topics to be viewed or created.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetailAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific topic to be retrieved, updated, or deleted.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'topic_uuid'


class TaskAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or created.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific task to be retrieved, updated, or deleted.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'task_uuid'


class TaskListAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows tasklists to be viewed or created.
    """
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListDetailAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific tasklist to be retrieved, updated, or deleted.
    """
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    lookup_field = 'list_uuid'
