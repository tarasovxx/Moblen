from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

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
        course_name = request.data.get('course_name')
        if not owner_uuid:
            return Response({"error": "NO_OWNER_UUID_IN_URL"}, status=status.HTTP_400_BAD_REQUEST)
        if not course_name:
            return Response({"error": "course_name is required in the request."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course(owner_uuid=owner_uuid, course_name=course_name)
            course.save()

        except IntegrityError as e:
            return Response({"status": "RECORD_ALREADY_EXISTS"}, status=status.HTTP_200_OK)

        return Response({"status": "SUCCESSFULLY_ADDED"},
                        status=status.HTTP_201_CREATED)


class CourseTutorAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific course to be retrieved, updated, or deleted.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'owner_uuid'


