from rest_framework import serializers

from .models import Course, Topic, Task, TaskList


class CourseSerializer(serializers.ModelSerializer):
    course_uuid = serializers.ReadOnlyField()
    owner_uuid = serializers.ReadOnlyField()

    class Meta:
        model = Course
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
