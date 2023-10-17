import hashlib

import django
from rest_framework import status
from rest_framework.response import Response

from .models import CustomUser
from customers.models import Student, Tutor
from customers.serializers import StudentSerializer, TutorSerializer


def authenticate_user(request, serializer_class):
    def auth_session(request, user_uuid):
        user = CustomUser.objects.get(user_uuid=user_uuid)  # Замените 'username' на имя пользователя
        django.contrib.auth.logout(request)
        django.contrib.auth.login(request, user)

    serializer = serializer_class(data=request.data)

    if not serializer.is_valid():
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    login = serializer.validated_data["login"]
    password = serializer.validated_data["password"]

    user = None
    if "@" in login:
        user = Student.objects.filter(email=login).first()
        if not user:
            user = Tutor.objects.filter(email=login).first()
    else:
        user = Student.objects.filter(phone_number=login).first()
        if not user:

            user = Tutor.objects.filter(phone_number=login).first()

    if not user:
        return Response({"error": "NO_SUCH_USER"}, status=status.HTTP_204_NO_CONTENT)

    salt = user.salt
    password_hash = user.password_hash

    password_with_salt = password + salt
    password_hash_input = hashlib.sha256(password_with_salt.encode()).hexdigest()

    if password_hash_input == password_hash:
        if isinstance(user, Student):
            print(request.user)
            if request.user.is_authenticated:
                print('1')
                return Response({"status": "ALREADY_AUTHORIZED"}, status=status.HTTP_400_BAD_REQUEST)
            auth_session(request, user.student_uuid)
            return Response({"status": "AUTHORIZED", "role": "student", "user": StudentSerializer(user).data},
                            status=status.HTTP_200_OK)
        elif isinstance(user, Tutor):
            if request.user.is_authenticated:
                return Response({"status": "ALREADY_AUTHORIZED"}, status=status.HTTP_400_BAD_REQUEST)
            auth_session(request, user.tutor_uuid)
            return Response({"status": "AUTHORIZED", "role": "tutor", "user": TutorSerializer(user).data},
                            status=status.HTTP_200_OK)

    return Response({"error": "INCORRECT_PASSWORD"}, status=status.HTTP_403_FORBIDDEN)