from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Course, Topic, Task, TaskList
from customers.models import Tutor

from .serializers import CourseSerializer, TopicSerializer, TaskSerializer, TaskListSerializer, TutorSerializer, CourseGetSerializer

import uuid


class CourseAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or created by tutor UUID.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'owner_uuid'


    def list(self, request, owner_uuid=None):
        try:
            tutor = Tutor.objects.get(tutor_uuid=owner_uuid)
        except Tutor.DoesNotExist:
            return Response({"error": "NO_SUCH_TUTOR"}, status=status.HTTP_404_NOT_FOUND)
        courses = Course.objects.filter(owner_uuid=tutor)

        courses_for_tutor = [course.course_name for course in courses]

        return Response(courses_for_tutor)


    def create(self, request, owner_uuid=None):
        course_name = request.data.get('course_name')
        if not owner_uuid:
            return Response({"error": "NO_OWNER_UUID_IN_URL"}, status=status.HTTP_400_BAD_REQUEST)
        if not course_name:
            return Response({"error": "course_name is required in the request."}, status=status.HTTP_400_BAD_REQUEST)

        tutor = get_object_or_404(Tutor, tutor_uuid=owner_uuid)

        try:
            course = Course(owner_uuid=tutor, course_name=course_name)
            course.save()

        except IntegrityError as e:
            return Response({"status": "RECORD_ALREADY_EXISTS"}, status=status.HTTP_200_OK)

        return Response({"status": "SUCCESSFULLY_ADDED"},
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, owner_uuid=None, course_uuid=None):
        try:
            tutor = Tutor.objects.get(tutor_uuid=owner_uuid)
        except Tutor.DoesNotExist:
            return Response({"error": "NO_SUCH_TUTOR"}, status=status.HTTP_404_NOT_FOUND)

        try:
            course = Course.objects.get(owner_uuid=tutor, course_uuid=course_uuid)
        except Course.DoesNotExist:
            return Response({"error": "NO_SUCH_COURSE"}, status=status.HTTP_404_NOT_FOUND)

        course.delete()
        return Response({"status": "SUCCESSFULLY_DELETED"}, status=status.HTTP_204_NO_CONTENT)




class CourseTutorAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific course to be retrieved, updated, or deleted.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'owner_uuid'


