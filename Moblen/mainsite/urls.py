from django.urls import path
from . import views
from .views import ReferralLinkAPIView

urlpatterns = [
    path('v1/getRef/', ReferralLinkAPIView.as_view({'post': 'create'}), name="get_ref_for_tutor")
]
