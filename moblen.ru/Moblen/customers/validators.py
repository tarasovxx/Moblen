from django.core.validators import EmailValidator
from rest_framework import serializers
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
        raise serializers.ValidationError({"error": str(e)})


def validate_phone(phone: int):
    if phone is None:
        return
    phone = str(phone)
    result = re.match(
        r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', phone)
    if not bool(result):
        raise serializers.ValidationError({"error": "INCORRECT_PHONE_NUMBER"})


def validate_pass_hash(password_hash: str):
    if password_hash is None:
        return
    if len(password_hash) != 64:
        raise serializers.ValidationError({'error': "HASH_LENGTH_MUST_BE_64"})


def validate_reflink(reflink: str):
    try:
        StudentGroup.objects.get(url=reflink)
    except StudentGroup.DoesNotExist:
        raise serializers.ValidationError({'error': "NO_SUCH_REFERRAL_LINK"})
