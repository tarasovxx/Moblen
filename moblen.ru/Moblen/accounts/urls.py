from django.urls import path
from .api import LogoutAPIView, LoginAPIView

urlpatterns = [
    # POST
    path('v1/users/login/', LoginAPIView.as_view({'post': "create"})),
    # POST
    path('v1/users/logout/', LogoutAPIView.as_view({'post': "post"})),
]
