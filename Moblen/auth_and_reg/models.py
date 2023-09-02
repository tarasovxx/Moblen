import uuid
from django.db import models


# Create your models here.
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
