from requests import Response
from rest_framework import viewsets, status
from .models import ReferralLink
from .serializers import ReferralLinkSerializer


class ReferralLinkAPIView(viewsets.ModelViewSet):
    queryset = ReferralLink.objects.all()
    serializer_class = ReferralLinkSerializer

    def get_ref_for_tutor(self, request):
        serializer = ReferralLinkSerializer(data=request.data)
        if serializer.is_valid():
            owner_uuid = serializer.validated_data['owner_uuid']
            group_uuid = serializer.validated_data['group_uuid']
            ref = ReferralLink.objects.filter(owner_uuid=owner_uuid, group_uuid=group_uuid)


        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


