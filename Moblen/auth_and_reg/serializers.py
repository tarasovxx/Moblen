from django.core.validators import EmailValidator, validate_email
from rest_framework import serializers

from .models import Tutor, Student, StudentTutorRelationship


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"

    def validate(self, data):
        #  Проверяем email
        email = data.get("email")
        validate_email(email)

        return data
