from django.core.validators import EmailValidator
from rest_framework import serializers
import re


def validate_email(email):
    if email is None:
        return
    email_validator = EmailValidator()
    try:
        email_validator(email)
    except serializers.ValidationError as e:
        # Обработка ошибки валидации email
        raise serializers.ValidationError({"email": str(e)})


def validate_phone(phone):
    if phone is None:
        return
    phone = str(phone)
    result = re.match(
        r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', phone)
    if not bool(result):
        raise serializers.ValidationError({"phone_number": "Incorrect phone number"})


def validate_pass_hash(password_hash):
    if password_hash is None:
        return
    if len(password_hash) != 64:
        raise serializers.ValidationError({'password_hash': "The hash looks incorrect"})
