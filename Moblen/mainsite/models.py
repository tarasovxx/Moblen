import os
import uuid
from django.db import models

from django.utils import timezone

from dotenv import load_dotenv

from auth_and_reg.models import StudentGroup
from courses.models import TaskList

load_dotenv()
domain = os.getenv('DOMAIN')

class TaskListGroupRelationship(models.Model):
    list_uuid = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    group_uuid = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)



