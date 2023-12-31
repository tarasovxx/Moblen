import uuid

from django.db import models

from customers.models import Tutor

# Create your models here.
class Course(models.Model):
    course_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner_uuid = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)

class Topic(models.Model):
    topic_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_uuid = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=50)


class TaskList(models.Model):
    list_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic_uuid = models.ForeignKey(Topic, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=50)

class Task(models.Model):
    task_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list_uuid = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    task_condition = models.TextField()
    task_image = models.BinaryField(null=True, blank=True)
    criteria = models.TextField()
    max_ball = models.IntegerField()
    format = models.TextField()
