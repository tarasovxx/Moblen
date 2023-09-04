from django.core.validators import EmailValidator
from .models import Tutor, Student, StudentTutorRelationship
from rest_framework import serializers

from .validators import validate_email, validate_phone


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"

    def validate(self, data):
        #  Проверяем email
        email = data.get("email")
        validate_email(email)
        #  Проверяем номер телефона
        phone = data.get('phone_number')
        validate_phone(str(phone))

        return data
