from django.urls import path
from . import views

urlpatterns = [
    path('registry/', views.registry),
    path('registry/success/', views.registration_success, name='registration_success'),
]
