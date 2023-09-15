import os
import uuid

from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from customers.models import Tutor, Student
from .models import StudentGroup, StudentGroupRelationship
from .serializers import TutorsGroupSerializer, StudentGroupRelationshipSerializer, \
    StudentGroupRelationshipCreateSerializer, ReferralLinkSerializer
from customers.serializers import StudentSerializer
from dotenv import load_dotenv

load_dotenv()
domain = os.getenv('DOMAIN')


def generate_unique_url():
    return f"http://{domain}/ref/{uuid.uuid4()}"


class TutorsGroupAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows Tutor groups to be created or viewed.
    """
    queryset = StudentGroup.objects.all()
    serializer_class = TutorsGroupSerializer
    lookup_field = 'owner_uuid'

    def create(self, request, owner_uuid=None):
        group_name = request.data.get('group_name')
        if not group_name:
            return Response({"error": "group_name is required in the request."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            tutor = Tutor.objects.get(tutor_uuid=owner_uuid)
        except Tutor.DoesNotExist:
            return Response({"error": "NO_SUCH_TUTOR"})

        student_group = StudentGroup(owner_uuid=tutor, group_name=group_name, url=generate_unique_url())
        student_group.save()

        serializer = TutorsGroupSerializer(student_group)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TutorsGroupDetailAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows specific Tutor group to be edited or deleted.
    """
    queryset = StudentGroup.objects.all()
    serializer_class = TutorsGroupSerializer
    lookup_field = 'group_uuid'


class StudentInGroup(viewsets.ModelViewSet):
    """
    API endpoint that allows you to add a student to a group
    """
    queryset = StudentGroupRelationship.objects.all()
    serializer_class = StudentGroupRelationshipSerializer
    lookup_field = 'group_uuid'

    @swagger_auto_schema(responses={200: StudentSerializer(many=True)})
    def list(self, request, group_uuid=None):
        try:
            group = StudentGroup.objects.get(group_uuid=group_uuid)
        except StudentGroup.DoesNotExist:
            return Response({"error": "NO_SUCH_STUDENT_GROUP"}, status=status.HTTP_404_NOT_FOUND)

        # Получите связи StudentGroupRelationship для указанной группы
        relationships = StudentGroupRelationship.objects.filter(group=group)

        # Извлеките список студентов из связей
        students = [relationship.student for relationship in relationships]

        # Сериализуйте список студентов и верните их в ответе
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=StudentGroupRelationshipCreateSerializer, responses={201: "SUCCESSFULLY_ADDED"})
    def create(self, request, group_uuid=None):
        serializer = StudentGroupRelationshipCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        student_uuid = serializer.validated_data['student_uuid']

        try:
            group = StudentGroup.objects.get(group_uuid=group_uuid)
        except StudentGroup.DoesNotExist:
            return Response({"error": "Group not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExits:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        # Создать новую связь StudentGroupRelationship
        try:
            relationship = StudentGroupRelationship(group=group, student=student)
            relationship.save()
        except IntegrityError as e:
            return Response({"status": "RECORD_ALREADY_EXIST"}, status=status.HTTP_200_OK)

        return Response({"status": "SUCCESSFULLY_ADDED"},
                        status=status.HTTP_201_CREATED)


class DeleteAStudentFromTheGroup(viewsets.ModelViewSet):
    """
    API that allows you to remove a student from a group
    """
    queryset = StudentGroupRelationship.objects.all()
    serializer_class = StudentGroupRelationshipSerializer

    def destroy(self, request, group_uuid=None, student_uuid=None):
        try:
            group = StudentGroup.objects.get(group_uuid=group_uuid)
        except StudentGroup.DoesNotExits:
            return Response({"error": "NO_SUCH_STUDENT_GROUP"}, status=status.HTTP_404_NOT_FOUND)
        try:
            student = Student.objects.get(student_uuid=student_uuid)
        except Student.DoesNotExits:
            return Response({"error": "NO_SUCH_STUDENT"}, status=status.HTTP_404_NOT_FOUND)

        try:
            relationship = StudentGroupRelationship.objects.get(group=group, student=student)
        except StudentGroupRelationship.DoesNotExist:
            return Response({"error": "NO_SUCH_RELATIONSHIP"}, status=status.HTTP_404_NOT_FOUND)

        relationship.delete()

        return Response({"status": "SUCCESSFULLY_DELETED"}, status=status.HTTP_202_ACCEPTED)


class ReferralLinkAPIView(viewsets.ModelViewSet):
    """
    API that allows you to get a referral link for a group
    """
    queryset = StudentGroup.objects.all()
    serializer_class = ReferralLinkSerializer

    def retrieve(self, request, group_uuid=None):
        try:
            student_group = StudentGroup.objects.get(group_uuid=group_uuid)
        except StudentGroup.DoesNotExist:
            return Response({"error": "NO_SUCH_STUDENT_GROUP"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReferralLinkSerializer(student_group)
        return Response({'url': serializer.data['url']})

    @action(detail=True, methods=['patch'])
    @swagger_auto_schema(operation_description="This request does not require a request body.")
    def regenerate_url(self, owner_uuid=None, group_uuid=None):
        if group_uuid is None:
            return Response({"error": "NO_GROUP_UUID_IN_URL"},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            student_group = StudentGroup.objects.get(group_uuid=group_uuid)
        except StudentGroup.DoesNotExist:
            return Response({"error": "NO_SUCH_STUDENT_GROUP"}, status=status.HTTP_404_NOT_FOUND)

        # Перегенерируйте поле 'url' и сохраните объект
        student_group.url = f"http://{domain}/ref/{uuid.uuid4()}"
        student_group.save()

        serializer = ReferralLinkSerializer(student_group)
        return Response({'url': serializer.data['url']})
