from rest_framework import serializers
from customers.serializers import StudentSerializer
from .models import StudentGroup, StudentGroupRelationship


class SwagTutorsGroupSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = StudentGroup
        fields = ("group_uuid", "group_name", "url", "students")


class TutorsGroupSerializer(serializers.ModelSerializer):
    url = serializers.ReadOnlyField()

    class Meta:
        model = StudentGroup
        fields = ("group_uuid", "group_name", "url")


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
