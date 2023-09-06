from django.shortcuts import render
from rest_framework import viewsets
from .models import Tutor, Student, StudentTutorRelationship, StudentGroup, StudentGroupRelationship
from .serializers import TutorSerializer


# Create your views here.
class TutorAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows tutors to be viewed or edited.
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


