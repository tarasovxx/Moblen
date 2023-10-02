import hashlib
import os
import random
import string

from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Tutor, Student, StudentTutorRelationship
from .serializers import StudentSerializer, PostStudentSerializer, AttachStudentToTutorSerializer, \
    StudentTutorRelationshipSerializer, PostTutorSerializer, TutorSerializer, RegStudentByRefLinkSerializer, \
    CheckUserSerializer, SwagCheckUserSerializer, SwagStudentSerializer

from dotenv import load_dotenv

from groups.models import StudentGroup

from groups.models import StudentGroupRelationship

load_dotenv()
domain = os.getenv('DOMAIN')

import customers.func


# Create your views here.
class TutorAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows tutors to be viewed or created.
    """
    queryset = Tutor.objects.all()
    serializer_class = PostTutorSerializer

    def create(self, request, *args, **kwargs):
        # Получаем данные из запроса
        data = request.data

        # Передаем данные через сериализатор для валидации
        serializer = PostTutorSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        login = data.get("login")
        email = None
        phone_number = None

        if "@" in login:
            email = login
        else:
            phone_number = login

        if email:
            existing_tutor = Tutor.objects.filter(email=email).first()
            if existing_tutor:
                return Response({"error": "USER_WITH_THIS_EMAIL_ALREADY_EXISTS"},
                                status=status.HTTP_400_BAD_REQUEST)

        if phone_number:
            existing_tutor = Tutor.objects.filter(phone_number=phone_number).first()
            if existing_tutor:
                return Response({"error": "USER_WITH_THIS_PHONE_NUMBER_ALREADY_EXISTS"},
                                status=status.HTTP_400_BAD_REQUEST)

        # Генерируем случайную строку (salt)
        salt = ''.join(random.choices(string.ascii_letters + string.digits, k=36))

        # Хешируем пароль с использованием salt
        password = data.get("password")
        password_with_salt = password + salt
        password_hash = hashlib.sha256(password_with_salt.encode()).hexdigest()

        # Создаем новый объект Tutor
        tutor = Tutor.objects.create(
            tutor_name=data.get("tutor_name"),
            tutor_surname=data.get("tutor_surname"),
            phone_number=phone_number,
            email=email,
            password_hash=password_hash,
            salt=salt
        )
        tutor.save()
        tutor_json = TutorSerializer(tutor)

        return Response(tutor_json.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(responses={200: TutorSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(tutors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TutorDetailAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific tutor to be retrieved, updated, or deleted.
    """
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    lookup_field = 'tutor_uuid'


class StudentAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or created.
    """
    queryset = Student.objects.all()
    serializer_class = PostStudentSerializer

    def create(self, request, *args, **kwargs):
        # Получаем данные из запроса
        data = request.data

        # Передаем данные через сериализатор для валидации
        serializer = PostStudentSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        login = data.get("login")
        email = None
        phone_number = None

        if "@" in login:
            email = login
        else:
            phone_number = login

        if email:
            existing_student = Student.objects.filter(email=email).first()
            if existing_student:
                return Response({"error": "USER_WITH_THIS_EMAIL_ALREADY_EXISTS"},
                                status=status.HTTP_400_BAD_REQUEST)

        if phone_number:
            existing_student = Student.objects.filter(phone_number=phone_number).first()
            if existing_student:
                return Response({"error": "USER_WITH_THIS_PHONE_NUMBER_ALREADY_EXISTS"},
                                status=status.HTTP_400_BAD_REQUEST)

        # Генерируем случайную строку (salt)
        salt = ''.join(random.choices(string.ascii_letters + string.digits, k=36))

        # Хешируем пароль с использованием salt
        password = data.get("password")
        password_with_salt = password + salt
        password_hash = hashlib.sha256(password_with_salt.encode()).hexdigest()

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

        return Response(student_json.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(responses={200: StudentSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentDetailAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific student to be retrieved, updated, or deleted.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'student_uuid'

    @swagger_auto_schema(responses={200: SwagStudentSerializer})
    def retrieve(self, request, student_uuid=None):
        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExist:
            return Response({"error": "NO_SUCH_STUDENT"}, status=status.HTTP_404_NOT_FOUND)

        # Получите связи StudentGroupRelationship для указанной группы
        relationships = StudentTutorRelationship.objects.filter(student=student)

        # Извлеките список тьюторов из связей
        tutors = [relationship.tutor for relationship in relationships]

        # Сериализуйте список тьюторов и верните их в ответе
        serializer = TutorSerializer(tutors, many=True)
        resp = StudentSerializer(student).data
        resp.update({"tutors": serializer.data})
        return Response(resp)


class AttachStudentToTutorAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows tutor attach a new student to student's list
    """
    queryset = StudentTutorRelationship.objects.all()
    serializer_class = AttachStudentToTutorSerializer
    lookup_field = 'tutor_uuid'

    def create(self, request, tutor_uuid=None):
        serializer = AttachStudentToTutorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        student_uuid = serializer.validated_data['student_uuid']

        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExits:
            return Response({"error": "NO_SUCH_STUDENT"}, status=status.HTTP_404_NOT_FOUND)
        try:
            tutor = Tutor.objects.get(tutor_uuid=tutor_uuid)
        except Tutor.DoesNotExist:
            return Response({"error": "NO_SUCH_TUTOR"}, status=status.HTTP_404_NOT_FOUND)

        try:
            relationship = StudentTutorRelationship(tutor=tutor, student=student)
            relationship.save()
        except IntegrityError as e:
            return Response({"status": "RECORD_ALREADY_EXIST"}, status=status.HTTP_200_OK)

        return Response({"status": "SUCCESSFULLY_ADDED"},
                        status=status.HTTP_201_CREATED)


class DeleteStudentFromTutorAPIView(viewsets.ModelViewSet):
    """
    API which allows you to detach a student from a tutor
    """
    queryset = StudentTutorRelationship.objects.all()
    serializer_class = StudentTutorRelationshipSerializer

    def destroy(self, request, tutor_uuid=None, student_uuid=None):
        try:
            tutor = Tutor.objects.get(tutor_uuid=tutor_uuid)
        except Tutor.DoesNotExits:
            return Response({"error": "NO_SUCH_TUTOR"}, status=status.HTTP_404_NOT_FOUND)
        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExits:
            return Response({"error": "NO_SUCH_STUDENT"}, status=status.HTTP_404_NOT_FOUND)

        try:
            relationship = StudentTutorRelationship.objects.get(tutor=tutor, student=student)
        except StudentTutorRelationship.DoesNotExist:
            return Response({"error": "NO_SUCH_RELATIONSHIP"}, status=status.HTTP_404_NOT_FOUND)

        relationship.delete()

        return Response({"status": "SUCCESSFULLY_DELETED"}, status=status.HTTP_202_ACCEPTED)


class GetStudentsByTutorUuidAPIView(AttachStudentToTutorAPIView):
    """
    API that allows you to get a list of students from a specific tutor
    """
    queryset = StudentTutorRelationship.objects.all()
    serializer_class = StudentTutorRelationshipSerializer
    lookup_field = 'tutor_uuid'

    @swagger_auto_schema(responses={200: StudentSerializer(many=True)})
    def list(self, request, tutor_uuid=None):
        try:
            tutor = Tutor.objects.get(tutor_uuid=tutor_uuid)
        except Tutor.DoesNotExist:
            return Response({"error": "NO_SUCH_TUTOR"}, status=status.HTTP_404_NOT_FOUND)

        # Получите связи StudentGroupRelationship для указанной группы
        relationships = StudentTutorRelationship.objects.filter(tutor=tutor)

        # Извлеките список студентов из связей
        students = [relationship.student for relationship in relationships]

        # Сериализуйте список студентов и верните их в ответе
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class RegStudentByRefLinkAPIView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = RegStudentByRefLinkSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            #  Забираем реферальную ссылку
            reflink = serializer.validated_data.pop("referral_link")

            #  Сохраняем нового ученика
            login = data.get("login")
            email = None
            phone_number = None

            if "@" in login:
                email = login
            else:
                phone_number = login

            if email:
                existing_student = Student.objects.filter(email=email).first()
                if existing_student:
                    return Response({"error": "USER_WITH_THIS_EMAIL_ALREADY_EXISTS"},
                                    status=status.HTTP_400_BAD_REQUEST)

            if phone_number:
                existing_student = Student.objects.filter(phone_number=phone_number).first()
                if existing_student:
                    return Response({"error": "USER_WITH_THIS_PHONE_NUMBER_ALREADY_EXISTS"},
                                    status=status.HTTP_400_BAD_REQUEST)

            # Генерируем случайную строку (salt)
            salt = ''.join(random.choices(string.ascii_letters + string.digits, k=36))

            # Хешируем пароль с использованием salt
            password = data.get("password")
            password_with_salt = password + salt
            password_hash = hashlib.sha256(password_with_salt.encode()).hexdigest()

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

            #  Находим группу и тьютора по реферальной ссылке
            group = StudentGroup.objects.get(url=reflink)
            tutor = Tutor.objects.get(tutor_uuid=group.owner_uuid.tutor_uuid)

            #  Формируем связи
            relationship_with_tutor = StudentTutorRelationship(student=student, tutor=tutor)
            relationship_with_group = StudentGroupRelationship(student=student, group=group)
            relationship_with_tutor.save()
            relationship_with_group.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'status': 'SUCCESSFULLY_ADDED', "student": student_json.data}, status=status.HTTP_201_CREATED)


class CheckUserAPIView(viewsets.ModelViewSet):
    serializer_class = CheckUserSerializer

    @swagger_auto_schema(responses={200: SwagCheckUserSerializer})
    def update(self, request):
        return func.authenticate_user(request, self.serializer_class)


