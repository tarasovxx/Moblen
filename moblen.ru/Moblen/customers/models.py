import os
import uuid
from django.db import models
from dotenv import load_dotenv
load_dotenv()
domain = os.getenv('DOMAIN')


# Create your models here.
class Tutor(models.Model):
    tutor_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tutor_name = models.CharField(max_length=30)
    tutor_surname = models.CharField(max_length=30)
    tutor_photo = models.BinaryField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    has_access = models.BooleanField(default=False)
    password_hash = models.CharField(max_length=257)
    salt = models.CharField(max_length=36)

    def __str__(self):
        return f"{self.tutor_name} {self.tutor_surname} ☎️ {self.phone_number}"


class Student(models.Model):
    student_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_name = models.CharField(max_length=30)
    student_surname = models.CharField(max_length=30)
    student_photo = models.BinaryField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    password_hash = models.CharField(max_length=257)
    salt = models.CharField(max_length=36)

    def __str__(self):
        return f"{self.student_name} {self.student_surname} ☎️ {self.phone_number}"


class StudentTutorRelationship(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'tutor')



