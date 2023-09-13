from django.urls import path

from .views import TutorsGroupDetailAPIView, StudentGroupRelationshipAPIView, ReferralLinkAPIView, \
    TutorsGroupAPIView

urlpatterns = [
    path('v1/group/<uuid:group_uuid>/', TutorsGroupDetailAPIView.as_view({'patch': 'partial_update',
                                                                          'delete': 'destroy'})),
    path('v1/group/<uuid:group_uuid>/students-in-group/', StudentGroupRelationshipAPIView.as_view({'get': 'list',
                                                                                                   'post': 'create'})),
    path('v1/reflink/<uuid:owner_uuid>/<uuid:group_uuid>/', ReferralLinkAPIView.as_view({'get': 'retrieve',
                                                                                         'patch': 'regenerate_url'},
                                                                                        name="get_ref_link")),
    path('v1/group/get-or-post-by-owner-uuid/<uuid:owner_uuid>/', TutorsGroupAPIView.as_view({
        'get': 'list',
        'post': 'create'})),

]