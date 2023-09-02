from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from auth_and_reg.views import TutorAPIView

router = routers.DefaultRouter()
router.register(r'api/v1/tutor', TutorAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainsite.urls")),
    path('', include(router.urls))
]
