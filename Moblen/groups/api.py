import os
import uuid

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


# Create your views here.
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
            return Response({"error": "Tutor not found."})

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


class StudentGroupRelationshipAPIView(viewsets.ModelViewSet):
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
            return Response({"error": "Group not found."}, status=status.HTTP_404_NOT_FOUND)

        # Получите связи StudentGroupRelationship для указанной группы
        relationships = StudentGroupRelationship.objects.filter(group=group)

        # Извлеките список студентов из связей
        students = [relationship.student for relationship in relationships]

        # Сериализуйте список студентов и верните их в ответе
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=StudentGroupRelationshipCreateSerializer, responses={201: "the student has been "
                                                                                                "successfully added "
                                                                                                "to the group"})
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
        relationship = StudentGroupRelationship(group=group, student=student)
        relationship.save()

        return Response({"status": "the student has been successfully added to the group"},
                        status=status.HTTP_201_CREATED)


class ReferralLinkAPIView(viewsets.ModelViewSet):
    """
    API that allows you to get a referral link for a group
    """
    queryset = StudentGroup.objects.all()
    serializer_class = ReferralLinkSerializer

    def retrieve(self, request, owner_uuid=None, group_uuid=None):
        if owner_uuid is None or group_uuid is None:
            return Response({"error": "Owner_uuid and Group_uuid must be provided in the URL."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            student_group = StudentGroup.objects.get(owner_uuid=owner_uuid, group_uuid=group_uuid)
        except StudentGroup.DoesNotExist:
            return Response({"error": "StudentGroup not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReferralLinkSerializer(student_group)  # Используйте ваш сериализатор для сериализации объекта
        return Response({'url': serializer.data['url']})

    @action(detail=True, methods=['patch'])
    @swagger_auto_schema(operation_description="This request does not require a request body.")
    def regenerate_url(self, request, owner_uuid=None, group_uuid=None):
        if owner_uuid is None or group_uuid is None:
            return Response({"error": "Owner_uuid and Group_uuid must be provided in the URL."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            student_group = StudentGroup.objects.get(owner_uuid=owner_uuid, group_uuid=group_uuid)
        except StudentGroup.DoesNotExist:
            return Response({"error": "StudentGroup not found"}, status=status.HTTP_404_NOT_FOUND)

        # Перегенерируйте поле 'url' и сохраните объект
        student_group.url = f"http://{domain}/ref/{uuid.uuid4()}"
        student_group.save()

        serializer = ReferralLinkSerializer(student_group)  # Используйте ваш сериализатор для сериализации объекта
        return Response({'url': serializer.data['url']})