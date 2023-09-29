from django.core.validators import EmailValidator
from rest_framework import serializers, validators
import re

from groups.models import StudentGroup


def validate_email(email: str):
    if email is None:
        return
    email_validator = EmailValidator()
    try:
        email_validator(email)
    except serializers.ValidationError as e:
        # Обработка ошибки валидации email
        raise serializers.ValidationError({"error": "INCORRECT_EMAIL"})


def validate_phone(phone: int):
    if phone is None:
        return
    phone = str(phone)
    result = re.match(
        r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', phone)
    if not bool(result):
        raise serializers.ValidationError({"error": "INCORRECT_PHONE_NUMBER"})


def validate_password(password: str):
    if password is None:
        return

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    if re.match(pattern, password) is None:
        raise serializers.ValidationError('PASSWORD_HAS_INCORRECT_FORMAT')


def validate_reflink(reflink: str):
    try:
        StudentGroup.objects.get(url=reflink)
    except StudentGroup.DoesNotExist:
        raise serializers.ValidationError({'error': "NO_SUCH_REFERRAL_LINK"})
