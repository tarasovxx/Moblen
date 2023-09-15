import os

from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Tutor, Student, StudentTutorRelationship
from .serializers import TutorSerializer, StudentSerializer, AttachStudentToTutorSerializer, \
    StudentTutorRelationshipSerializer, RegStudentByRefLinkSerializer

from dotenv import load_dotenv

load_dotenv()
domain = os.getenv('DOMAIN')


# Create your views here.
class TutorAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows tutors to be viewed or created.
    """
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


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
    serializer_class = StudentSerializer


class StudentDetailAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows a specific student to be retrieved, updated, or deleted.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'student_uuid'


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
        pass