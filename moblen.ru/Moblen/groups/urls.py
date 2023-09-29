from django.urls import path

from .api import TutorsGroupDetailAPIView, StudentInGroup, ReferralLinkAPIView, \
    TutorsGroupAPIView, DeleteAStudentFromTheGroup

urlpatterns = [
    #  GET, PATCH, DELETE
    path('v1/group/<uuid:group_uuid>/', TutorsGroupDetailAPIView.as_view({'get': 'retrieve',
                                                                          'patch': 'partial_update',
                                                                          'delete': 'destroy'})),
    # POST
    path('v1/student/in-the-group/<uuid:group_uuid>/', StudentInGroup.as_view({'post': 'create'})),

    #  DELETE
    path('v1/student/<uuid:student_uuid>/from-the-group/<uuid:group_uuid>/', DeleteAStudentFromTheGroup.as_view(
        {'delete': 'destroy'})),

    #  GET, PATCH
    path('v1/group/<uuid:group_uuid>/reflink/',
         ReferralLinkAPIView.as_view({'get': 'retrieve',
                                      'patch': 'regenerate_url'},
                                     name="get_or_update_ref_link")),
    #  GET, POST
    path('v1/tutor/<uuid:owner_uuid>/tutor-groups/', TutorsGroupAPIView.as_view({
        'get': 'list',
        'post': 'create'})),

]
