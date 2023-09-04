from django.core.validators import EmailValidator
from rest_framework import serializers
import re


def validate_email(email):
    email_validator = EmailValidator()
    try:
        email_validator(email)
    except serializers.ValidationError as e:
        # Обработка ошибки валидации email
        raise serializers.ValidationError({"email": str(e)})


def validate_phone(phone):
    result = re.match(
        r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', phone)
    if not bool(result):
        raise serializers.ValidationError({"phone_number": "Incorrect phone number"})

