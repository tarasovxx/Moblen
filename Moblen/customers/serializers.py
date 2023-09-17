
from .models import Tutor, Student, StudentTutorRelationship
from rest_framework import serializers

from .validators import validate_email, validate_phone, validate_pass_hash


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
        validate_phone(phone)
        #  Проверяем хэш.
        password_hash = data.get('password_hash')
        validate_pass_hash(password_hash)
        return data


class StudentSerializer(TutorSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class AttachStudentToTutorSerializer(serializers.Serializer):
    student_uuid = serializers.UUIDField()


class StudentTutorRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTutorRelationship
        fields = "__all__"


class RegStudentByRefLinkSerializer(StudentSerializer):
    referral_link = serializers.URLField(required=True)


