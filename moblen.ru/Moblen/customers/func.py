import hashlib
import random
import string

import django.contrib
import requests
from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.response import Response
from customers.models import Tutor, Student
from customers.serializers import StudentSerializer, TutorSerializer
from accounts.models import CustomUser


def post_new_user(request, serializer, role):
    # Получаем данные из запроса
    data = request.data

    serializer = serializer(data=data)

    if not serializer.is_valid():
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    login = serializer.validated_data["login"]

    user = None
    if "@" in login:
        phone_number = None
        email = login
        user = Student.objects.filter(email=login).first()
        if not user:
            user = Tutor.objects.filter(email=login).first()
    else:
        phone_number = login
        email = None
        user = Student.objects.filter(phone_number=login).first()
        if not user:
            user = Tutor.objects.filter(phone_number=login).first()

    if user:
        return Response({'status': "USER_WITH_THIS_LOGIN_ALREADY_EXISTS"}, status=status.HTTP_400_BAD_REQUEST)

    # Генерируем случайную строку (salt)
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=36))

    # Хешируем пароль с использованием salt
    password = data.get("password")
    password_with_salt = password + salt
    password_hash = hashlib.sha256(password_with_salt.encode()).hexdigest()

    if role == "ST":
        # Создаем новый объект Student
        student = Student.objects.create(
            student_name=data.get("student_name"),
            student_surname=data.get("student_surname"),
            phone_number=phone_number,
            email=email,
            password_hash=password_hash,
            salt=salt
        )
        student.save()
        student_json = StudentSerializer(student)

        base_user = CustomUser.objects.create(
            username=str(email)+"."+str(phone_number),
            first_name=data.get("student_name"),
            last_name=data.get("student_surname"),
            password=password_hash,
            role=role,
            user_uuid=student.student_uuid,
        )
        base_user.save()

        return Response(student_json.data, status=status.HTTP_201_CREATED)

    elif role == "TT":
        # Создаем новый объект Tutor
        tutor = Tutor.objects.create(
            tutor_name=data.get("tutor_name"),
            tutor_surname=data.get("tutor_surname"),
            phone_number=phone_number,
            email=email,
            password_hash=password_hash,
            salt=salt
        )

        tutor_json = TutorSerializer(tutor)

        base_user = CustomUser.objects.create(
            username=str(email)+"."+str(phone_number),
            first_name=data.get("tutor_name"),
            last_name=data.get("tutor_surname"),
            password=password_hash,
            role=role,
            user_uuid=tutor.tutor_uuid,
        )

        base_user.save()
        tutor.save()
        return Response(tutor_json.data, status=status.HTTP_201_CREATED)

