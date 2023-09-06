from django.urls import path
from .views import TutorAPIView, TutorDetailAPIView

urlpatterns = [
    path('v1/tutor/', TutorAPIView.as_view({'get': 'list', 'post': 'create'}), name="all_tutor_api"),
    path('v1/tutor/<uuid:tutor_uuid>/', TutorDetailAPIView.as_view({'get': 'retrieve'}), name="tutor_api"),
]
