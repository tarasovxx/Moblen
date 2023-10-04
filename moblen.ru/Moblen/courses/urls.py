from django.urls import path
from .api import CourseTutorAPIView, CourseAPIView  # , TopicCourseAPIView, TaskListTopicAPIView, TaskTasklistAPIView

urlpatterns = [
    path('v1/courses/by-tutor/<uuid:owner_uuid>/', CourseAPIView.as_view(
        {'get': 'list',
         'post': 'create'}),
         name="courses_api"),
    path('v1/courses/by-tutor/<uuid:owner_uuid>/<uuid:course_uuid>', CourseAPIView.as_view(
        {
         'delete': 'destroy'
        }),
         name="courses_api_delete"),
    #
    # path('v1/topic/by-course/<uuid:courses_uuid>/', TopicCourseAPIView.as_view(
    #     {'get': 'retrieve',
    #      'patch': 'partial_update',
    #      'delete': 'destroy'}),
    #      name="topic_api"),
    #
    # path('v1/tasklist/by-topic/<uuid:topic_uuid>/', TaskListTopicAPIView.as_view(
    #     {'get': 'retrieve',
    #      'patch': 'partial_update',
    #      'delete': 'destroy'}),
    #      name="courses_api"),
    #
    # path('v1/task/by-tasklist/<uuid:tasklist_uuid>/', TaskTasklistAPIView.as_view(
    #     {'get': 'retrieve',
    #      'patch': 'partial_update',
    #      'delete': 'destroy'}),
    #      name="task_api")
]