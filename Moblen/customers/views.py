import uuid
import os

from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Tutor, Student, StudentTutorRelationship
from .serializers import TutorSerializer, StudentSerializer

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




# class RegStudentByRefLinkAPIView(viewsets.ModelViewSet):
#     queryset = [Student.objects.all(), ReferralLink.objects.all(), StudentGroup.objects.all()]
#     serializer_class =
