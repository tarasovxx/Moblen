from django.core.validators import EmailValidator

from Moblen.auth_and_reg import serializers


def validate_email(email):
    email_validator = EmailValidator()
    try:
        email_validator(email)
    except serializers.ValidationError as e:
        # Обработка ошибки валидации email
        raise serializers.ValidationError({"email": str(e)})