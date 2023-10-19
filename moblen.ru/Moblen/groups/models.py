import uuid

from django.db import models

from courses.models import TaskList
from customers.models import Tutor, Student


class StudentGroup(models.Model):
    group_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner_uuid = models.ForeignKey(Tutor, on_delete=models.CASCADE, editable=False)
    group_name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return (f"{self.owner_uuid.tutor_name} {self.owner_uuid.tutor_surname}"
                f" ☎️ {self.owner_uuid.phone_number} 👨‍👨‍👦‍👦 {self.group_name}")


class StudentGroupRelationship(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'group')

    def __str__(self):
        return (f'Ученик: {self.student.phone_number}.'
                f' Находится в группе "{self.group.group_name}" преподавателя {self.group.owner_uuid.phone_number}')


class TaskListGroupRelationship(models.Model):
    list_uuid = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    group_uuid = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
