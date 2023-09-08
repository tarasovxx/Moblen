from django.contrib.auth.models import User
from django.db.models.signals import post_save
from auth_and_reg import Tutor, Student
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=Tutor)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
