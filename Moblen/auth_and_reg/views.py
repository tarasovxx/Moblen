import uuid
import os

from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Tutor, Student, StudentTutorRelationship, StudentGroup, StudentGroupRelationship
from .serializers import TutorSerializer, StudentSerializer, GroupSerializer, StudentGroupRelationshipSerializer, \
    ReferralLinkSerializer

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


class GroupAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or created.
    """
    queryset = StudentGroup.objects.all()
    serializer_class = GroupSerializer


class TutorsGroupAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows Tutor groups to be viewed.
    """
    queryset = StudentGroup.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'owner_uuid'


class StudentGroupRelationshipAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows you to add a student to a group
    """
    queryset = StudentGroupRelationship.objects.all()
    serializer_class = StudentGroupRelationshipSerializer


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

# class RegStudentByRefLinkAPIView(viewsets.ModelViewSet):
#     queryset = [Student.objects.all(), ReferralLink.objects.all(), StudentGroup.objects.all()]
#     serializer_class =
