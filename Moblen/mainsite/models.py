import os
import uuid
from django.db import models

from auth_and_reg.models import Tutor, StudentGroup
from django.utils import timezone

from dotenv import load_dotenv
load_dotenv()
domain=os.getenv('DOMAIN')


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


class TaskListGroupRelationship(models.Model):
    list_uuid = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    group_uuid = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)


class Task(models.Model):
    task_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic_uuid = models.ForeignKey(Topic, on_delete=models.CASCADE)
    task_condition = models.TextField()
    task_image = models.BinaryField(null=True, blank=True)
    task_answer = models.CharField(max_length=50)
    criteria = models.TextField()


class ReferralLink(models.Model):
    ref_id = models.AutoField(primary_key=True)  # INT AUTOINCREMENT
    owner_uuid = models.ForeignKey(Tutor, on_delete=models.CASCADE)  # Внешний ключ на модель Tutor
    group_uuid = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)  # Внешний ключ на модель StudentGroup
    url = models.URLField(editable=False, default="http://{}/ref/{}".format(domain, uuid.uuid4()))
    expires = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=2))
