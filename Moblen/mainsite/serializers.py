from rest_framework import serializers

from .models import ReferralLink


class ReferralLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralLink
        fields = ['owner_uuid', 'group_uuid', 'url']
