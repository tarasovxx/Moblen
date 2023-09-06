import hashlib
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from rest_framework.response import Response

from .models import ReferralLink
from .serializers import ReferralLinkSerializer


class ReferralLinkAPIView(viewsets.ModelViewSet):
    queryset = ReferralLink.objects.all()
    serializer_class = ReferralLinkSerializer

    def create(self, request, *args, **kwargs):
        owner_uuid = request.data.get('owner_uuid')
        group_uuid = request.data.get('group_uuid')

        # Проверяем наличие объекта ReferralLink с такими owner_uuid и group_uuid
        referral_link = get_object_or_404(
            ReferralLink, owner_uuid=owner_uuid, group_uuid=group_uuid, expires__gt=timezone.now()
        )

        # Если объект существует и expires еще не истек, возвращаем URL
        if referral_link:
            serializer = self.get_serializer(referral_link)
            return Response(serializer.data)

        # Если объект не существует или expires истек, создаем новый объект и возвращаем URL
        return super().create(request, *args, **kwargs)
