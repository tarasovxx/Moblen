import os
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Tutor, Student, StudentTutorRelationship
from .serializers import TutorSerializer, StudentSerializer, AttachStudentToTutorSerializer

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
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        try:
            tutor = Tutor.objects.get(tutor_uuid=tutor_uuid)
        except Tutor.DoesNotExist:
            return Response({"error": "Tutor not found."}, status=status.HTTP_404_NOT_FOUND)

        relationship = StudentTutorRelationship(tutor=tutor, student=student)
        relationship.save()

        return Response({"status": "The student is successfully attached to the tutor"},
                        status=status.HTTP_201_CREATED)



# class RegStudentByRefLinkAPIView(viewsets.ModelViewSet):
#     queryset = [Student.objects.all(), ReferralLink.objects.all(), StudentGroup.objects.all()]
#     serializer_class =
