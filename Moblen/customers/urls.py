from django.urls import path
from .api import TutorAPIView, TutorDetailAPIView, StudentAPIView, StudentDetailAPIView, AttachStudentToTutorAPIView, \
    GetStudentsByTutorUuidAPIView, DeleteStudentFromTutorAPIView, RegStudentByRefLinkAPIView

urlpatterns = [
    #  GET, POST
    path('v1/tutor/', TutorAPIView.as_view({'get': 'list',
                                            'post': 'create'}), name="all_tutors_api"),
    #  GET, PATCH, DELETE
    path('v1/tutor/<uuid:tutor_uuid>/', TutorDetailAPIView.as_view({'get': 'retrieve',
                                                                    'patch': 'partial_update',
                                                                    'delete': 'destroy'
                                                                    }), name="tutor_api"),
    #  POST
    path('v1/tutor/<uuid:tutor_uuid>/new-student-to-the-list/', AttachStudentToTutorAPIView.as_view({'post': 'create'})),
    # DELETE
    path('v1/student/<uuid:student_uuid>/from-the-tutor-list/<uuid:tutor_uuid>/', DeleteStudentFromTutorAPIView.as_view(
                                                                                                {'delete': 'destroy'})),

    #  GET, POST
    path('v1/student/', StudentAPIView.as_view({'get': 'list',
                                                'post': 'create'}), name="all_students_api"),
    #  GET, PATCH, DELETE
    path('v1/student/<uuid:student_uuid>/', StudentDetailAPIView.as_view({'get': 'retrieve',
                                                                          'patch': 'partial_update',
                                                                          'delete': 'destroy'
                                                                          }), name="student_api"),
    # GET
    path('v1/student/by-tutor-uuid/<uuid:tutor_uuid>/', GetStudentsByTutorUuidAPIView.as_view({'get': 'list'})),

    #  POST
    path('v1/student/with-ref-link/', RegStudentByRefLinkAPIView.as_view({'post': "create"})),


]
