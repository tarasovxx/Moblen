import hashlib

from rest_framework import status
from rest_framework.response import Response
from customers.models import Tutor, Student
from customers.serializers import StudentSerializer, TutorSerializer


#  Аутентификация юзера. Произвольная - любой роли.
def authenticate_user(request, serializer_class):
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

    if user:
        salt = user.salt
        password_hash = user.password_hash

        password_with_salt = password + salt
        password_hash_input = hashlib.sha256(password_with_salt.encode()).hexdigest()

        if password_hash_input == password_hash:
            if isinstance(user, Student):
                return Response({"status": "AUTHORIZED", "role": "student", "user": StudentSerializer(user).data},
                                status=status.HTTP_200_OK)
            elif isinstance(user, Tutor):
                return Response({"status": "AUTHORIZED", "role": "tutor", "user": TutorSerializer(user).data},
                                status=status.HTTP_200_OK)

    return Response({"error": "INCORRECT_PASSWORD"}, status=status.HTTP_400_BAD_REQUEST)