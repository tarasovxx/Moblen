from rest_framework import serializers
from customers.validators import validate_password
from customers.serializers import StudentSerializer

class CheckUserSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        validate_password(data.get('password'))
        return data


class SwagCheckUserSerializer(serializers.Serializer):
    status = serializers.CharField(read_only=True, default="AUTHORIZED", help_text=True)
    role = serializers.CharField(read_only=True, default="student", help_text=True)
    user = StudentSerializer()