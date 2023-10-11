from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Course, Topic, Task, TaskList
from customers.models import Tutor

from .serializers import CourseSerializer, TopicSerializer, TaskSerializer, TaskListSerializer, \
    CourseGetSerializer, TopicGetSerializer, TaskListGetSerializer

import uuid


class CourseByTutorAPIView(viewsets.ModelViewSet):
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

        courses_json = CourseGetSerializer(courses, many=True)

        return Response(courses_json.data)


    def create(self, request, owner_uuid=None):
        course_name = request.data.get('course_name')
        if not owner_uuid:
            return Response({"error": "NO_OWNER_UUID_IN_URL"}, status=status.HTTP_404_NOT_FOUND)
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


class TopicByCourseAPIView(viewsets.ModelViewSet):
    """
    API endpoint, which allows you to get all topics for the course, create a new one, delete.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'course_uuid'
    def list(self, request, course_uuid=None):
        try:
            course = Course.objects.get(course_uuid=course_uuid)
        except Course.DoesNotExist:
            return Response({"error": "NO_SUCH_COURSE"}, status=status.HTTP_404_NOT_FOUND)

        topics = Topic.objects.filter(course_uuid=course)
        topic_json = TopicGetSerializer(topics, many=True)
        return Response(topic_json.data)

    def create(self, request, course_uuid=None):
        topic_name = request.data.get('topic_name')
        if not course_uuid:
            return Response({"error": "NO_OWNER_COURSE_UUID_IN_URL"}, status=status.HTTP_404_NOT_FOUND)
        if not topic_name:
            return Response({"error": "topic_name is required in the request."}, status=status.HTTP_400_BAD_REQUEST)

        course = get_object_or_404(Course, course_uuid=course_uuid)

        try:
            topic = Topic(course_uuid=course, topic_name=topic_name)
            topic.save()

        except IntegrityError as e:
            return Response({"status": "RECORD_ALREADY_EXISTS"}, status=status.HTTP_200_OK)

        return Response({"status": "SUCCESSFULLY_ADDED"},
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, course_uuid=None, topic_uuid=None):
        try:
            course = Course.objects.get(course_uuid=course_uuid)
        except Course.DoesNotExist:
            return Response({"error": "NO_SUCH_COURSE"}, status=status.HTTP_404_NOT_FOUND)

        try:
            topic = Topic.objects.get(course_uuid=course, topic_uuid=topic_uuid)
        except Topic.DoesNotExist:
            return Response({"error": "NO_SUCH_TOPIC"}, status=status.HTTP_404_NOT_FOUND)

        topic.delete()
        return Response({"status": "SUCCESSFULLY_DELETED"}, status=status.HTTP_204_NO_CONTENT)


class TasklistByTopicAPIView(viewsets.ModelViewSet):
    """"
    API endpoint, which returns a sheet with specific tasks from a specific topic
    """
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    lookup_field = 'topic_uuid'

    def list(self, request, topic_uuid=None):
        try:
            topic = Topic.objects.get(topic_uuid=topic_uuid)
        except Topic.DoesNotExist:
            return Response({"error": "NO_SUCH_TOPIC"}, status=status.HTTP_404_NOT_FOUND)

        tasklists = TaskList.objects.filter(topic_uuid=topic)

        tasklist_json = TaskListGetSerializer(tasklists, many=True)

        return Response(tasklist_json.data)

    def create(self, request, topic_uuid=None):
        tasklist_name = request.data.get('list_name')
        if not topic_uuid:
            return Response({"error": "NO_OWNER_TOPIC_UUID_IN_URL"}, status=status.HTTP_404_NOT_FOUND)
        if not tasklist_name:
            return Response({"error": "list_name is required in the request."}, status=status.HTTP_400_BAD_REQUEST)

        topic = get_object_or_404(Topic, topic_uuid=topic_uuid)

        try:
            tasklist = TaskList(topic_uuid=topic, list_name=tasklist_name)
            tasklist.save()

        except IntegrityError as e:
            return Response({"status": "RECORD_ALREADY_EXISTS"}, status=status.HTTP_200_OK)

        return Response({"status": "SUCCESSFULLY_ADDED"},
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, topic_uuid=None, list_uuid=None):
        try:
            topic = Topic.objects.get(topic_uuid=topic_uuid)
        except Topic.DoesNotExist:
            return Response({"error": "NO_SUCH_TOPIC"}, status=status.HTTP_404_NOT_FOUND)

        try:
            tasklist = TaskList.objects.get(topic_uuid=topic, list_uuid=list_uuid)
        except TaskList.DoesNotExist:
            return Response({"error": "NO_SUCH_TASKLIST"}, status=status.HTTP_404_NOT_FOUND)

        tasklist.delete()
        return Response({"status": "SUCCESSFULLY_DELETED"}, status=status.HTTP_204_NO_CONTENT)


class TaskByTaskListAPIView(viewsets.ModelViewSet):
    """
    API endpoint, which receives all tasks in a specific task list, can create and delete them.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'list_uuid'

    def list(self, request, list_uuid=None):
        try:
            tasklist = TaskList.objects.get(list_uuid=list_uuid)
        except TaskList.DoesNotExist:
            return Response({"error": "NO_SUCH_TASKLIST"}, status=status.HTTP_404_NOT_FOUND)

        tasks = Task.objects.filter(list_uuid=tasklist)
        topic_uuid = tasklist.topic_uuid

        task_serializer = TaskSerializer(tasks, many=True)
        topic_serializer = TopicGetSerializer(instance=topic_uuid)

        response_data = {
            'topic_uuid': topic_serializer.data,  # Включаем topic_uuid в ответ
            'tasks': task_serializer.data,
        }
        # all_task_in_tasklist = [tasklist.list_name for tasklist in tasklists]

        return Response(response_data) # or tasks.data

    def create(self, request, list_uuid=None):
        if not list_uuid:
            return Response({"error": "NO_OWNER_TASKLIST_UUID_IN_URL"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        # Исключение!
        tasklist = get_object_or_404(TaskList, list_uuid=list_uuid)

        try:
            task = Task.objects.create(
                list_uuid=tasklist,
                task_condition=data.get('task_condition'),
                task_image=data.get('task_image'),  # Используем data.get()
                criteria=data.get('criteria'),
                max_ball=data.get('max_ball'),
                format=data.get('format')
            )
            task.save()
        except IntegrityError as e:
            return Response({"status": "RECORD_ALREADY_EXISTS"}, status=status.HTTP_200_OK)
        task_json = TaskSerializer(task)

        return Response(task_json.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, list_uuid=None, task_uuid=None):
        try:
            tasklist = TaskList.objects.get(list_uuid=list_uuid)
        except TaskList.DoesNotExist:
            return Response({"error": "NO_SUCH_TASKLIST"}, status=status.HTTP_404_NOT_FOUND)

        try:
            task = Task.objects.get(list_uuid=tasklist, task_uuid=task_uuid)
        except Task.DoesNotExist:
            return Response({"error": "NO_SUCH_TASK"}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({"status": "SUCCESSFULLY_DELETED"}, status=status.HTTP_204_NO_CONTENT)


