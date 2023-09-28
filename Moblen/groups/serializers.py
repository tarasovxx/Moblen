from rest_framework import serializers

from .models import StudentGroup, StudentGroupRelationship


class TutorsGroupSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()
    class Meta:
        model = StudentGroup
        fields = '__all__'


class StudentGroupRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroupRelationship
        fields = "__all__"


class StudentGroupRelationshipCreateSerializer(serializers.Serializer):
    student_uuid = serializers.UUIDField()


class ReferralLinkSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()
    class Meta:
        model = StudentGroup
        fields = ("url",)