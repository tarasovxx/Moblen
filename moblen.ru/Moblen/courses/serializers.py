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

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'
