from django.urls import path
from .views import TutorAPIView, TutorDetailAPIView, StudentAPIView, StudentDetailAPIView, GroupAPIView

urlpatterns = [
    path('v1/tutor/', TutorAPIView.as_view({'get': 'list',
                                            'post': 'create'}), name="all_tutors_api"),
    path('v1/tutor/<uuid:tutor_uuid>/', TutorDetailAPIView.as_view({'get': 'retrieve',
                                                                    'patch': 'partial_update',
                                                                    'delete': 'destroy'
                                                                    }), name="tutor_api"),
    path('v1/student/', StudentAPIView.as_view({'get': 'list',
                                                'post': 'create'}), name="all_students_api"),
    path('v1/student/<uuid:student_uuid>/', StudentDetailAPIView.as_view({'get': 'retrieve',
                                                                          'patch': 'partial_update',
                                                                          'delete': 'destroy'
                                                                          }), name="student_api"),
    path('v1/group/', GroupAPIView.as_view({'get': 'list',
                                                   'post': 'create'}, name="group_api"))
]
