from django.shortcuts import render
from rest_framework import viewsets
from .models import Tutor, Student, StudentTutorRelationship, StudentGroup, StudentGroupRelationship
from .serializers import TutorSerializer, StudentSerializer, CreateGroupSerializer, StudentGroupRelationshipSerializer


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
    API endpoint that allows a specific tutor to be retrieved, updated, or deleted.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'student_uuid'


class GroupAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or created.
    """
    queryset = StudentGroup.objects.all()
    serializer_class = CreateGroupSerializer


class StudentGroupRelationshipAPIView(viewsets.ModelViewSet):
    """
    The endpoint API that allows students to be added to or removed from a group.
    """
    queryset = StudentGroupRelationship.objects.all()
    serializer_class = StudentGroupRelationshipSerializer


# class RegStudentByRefLinkAPIView(viewsets.ModelViewSet):
#     queryset = [Student.objects.all(), ReferralLink.objects.all(), StudentGroup.objects.all()]
#     serializer_class =





