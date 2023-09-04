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
    http_method_names = ['get', 'post', 'path']




