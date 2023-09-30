
from .models import Tutor, Student, StudentTutorRelationship
from rest_framework import serializers

from .validators import validate_email, validate_phone, validate_password, validate_reflink


class PostTutorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    login = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Tutor
        fields = ('tutor_uuid', 'tutor_name', 'tutor_surname', 'login', 'password')

    def validate(self, data):
        #  Получаем логин
        login = data.get("login")
        email = None
        phone = None

        if "@" in login:
            email = login
            validate_email(email)
        else:
            phone = login
            validate_phone(phone)

        #  Проверяем пароль.
        password = data.get('password')
        validate_password(password)
        return data


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ('tutor_uuid', 'tutor_name', 'tutor_surname', 'tutor_photo',
                  'phone_number', 'email', 'has_access')


class PostStudentSerializer(PostTutorSerializer):

    class Meta:
        model = Student
        fields = ('student_uuid', 'student_name', 'student_surname', 'login', 'password')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_uuid', 'student_name', 'student_surname', 'student_photo',
                  'phone_number', 'email')


class AttachStudentToTutorSerializer(serializers.Serializer):
    student_uuid = serializers.UUIDField()


class StudentTutorRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTutorRelationship
        fields = "__all__"


class RegStudentByRefLinkSerializer(PostStudentSerializer):
    referral_link = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Student
        fields = ('referral_link', 'student_name', 'student_surname', 'login', 'password')

    def validate(self, data):
        #  Проверяем, что такая реферальная ссылка существует.
        validate_reflink(data.get("referral_link"))
        #  Выполняем те же проверки, что и в классах Tutor, Student
        super().validate(data)
        return data


class CheckUserSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        validate_password(data.get('password'))
        return data
