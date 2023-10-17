import django.contrib.auth
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializers import CheckUserSerializer, SwagCheckUserSerializer
from .func import authenticate_user


class LoginAPIView(viewsets.ModelViewSet):
    serializer_class = CheckUserSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: SwagCheckUserSerializer, 204: "NO_SUCH_USER"})
    def create(self, request):
        return authenticate_user(request, self.serializer_class)


class LogoutAPIView(viewsets.ModelViewSet):
    serializer_class = None
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(responses={200: None})
    def post(self, request):
        django.contrib.auth.logout(request)
        return Response({"detail": "Вы успешно разлогинились."}, status=status.HTTP_200_OK)