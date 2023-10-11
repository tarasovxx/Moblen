from rest_framework import serializers

from .models import Course, Topic, Task, TaskList
from customers.models import Tutor



class CourseSerializer(serializers.ModelSerializer):
    course_uuid = serializers.ReadOnlyField()
    owner_uuid = serializers.ReadOnlyField()

    class Meta:
        model = Course
        fields = '__all__'

class CourseGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_uuid', 'course_name')


class TopicSerializer(serializers.ModelSerializer):
    topic_uuid = serializers.ReadOnlyField()
    course_uuid = serializers.ReadOnlyField()
    class Meta:
        model = Topic
        fields = '__all__'

class TopicGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('topic_uuid', 'topic_name')


class TaskListSerializer(serializers.ModelSerializer):
    list_uuid = serializers.ReadOnlyField()
    topic_uuid = serializers.ReadOnlyField()
    class Meta:
        model = TaskList
        fields = '__all__'


class TaskListGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ('list_uuid', 'list_name')


class TaskSerializer(serializers.ModelSerializer):
#     task_condition = serializers.CharField(required=True, write_only=True)
#     task_image = serializers.CharField(required=True, write_only=True)
#     task_answer = serializers.CharField(required=True, write_only=True)
#     criteria = task_answer = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Task
        fields = ('task_uuid', 'task_condition', 'task_image', 'criteria', 'max_ball', 'format')

