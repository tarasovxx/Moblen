from django.db import models
from django.contrib.auth.models import User


# Создайте свои модели здесь.
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_uuid = models.UUIDField(blank=True, null=True)
    role = models.CharField(choices=[('ST', 'student'), ('TT', 'tutor')], blank=True, null=True, max_length=10)

