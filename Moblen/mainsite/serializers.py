from rest_framework import serializers

from .models import ReferralLink


class ReferralLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralLink
        fields = ['url']
