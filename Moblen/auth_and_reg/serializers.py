from rest_framework import serializers

from .models import Tutor, Student, StudentTutorRelationship


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"