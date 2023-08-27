from django.db import models
import uuid
# Create your models here.

from django.db import models


class Tutor(models.Model):
    tutor_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tutor_name = models.CharField(max_length=30)
    tutor_surname = models.CharField(max_length=30)
    tutor_photo = models.BinaryField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    has_access = models.BooleanField(default=False)
    password_hash = models.CharField(max_length=257)
    salt = models.CharField(max_length=36)


class Student(models.Model):
    student_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_name = models.CharField(max_length=30)
    student_surname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password_hash = models.BigIntegerField()
    salt = models.CharField(max_length=16)


class StudentTutorRelationship(models.Model):
    tutor_uuid = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student_uuid = models.ForeignKey(Student, on_delete=models.CASCADE)


class StudentGroup(models.Model):
    group_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner_uuid = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200)


class StudentGroupRelationship(models.Model):
    student_uuid = models.ForeignKey(Student, on_delete=models.CASCADE)
    group_uuid = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)


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
