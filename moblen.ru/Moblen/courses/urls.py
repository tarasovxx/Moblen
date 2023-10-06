from django.urls import path
from .api import CourseByTutorAPIView, TopicByCourseAPIView, TasklistByTopicAPIView, TaskByTaskListAPIView

urlpatterns = [
    path('v1/courses/by-tutor/<uuid:owner_uuid>/', CourseByTutorAPIView.as_view(
        {'get': 'list',
         'post': 'create'}),
         name="courses_by-tutor_api"),
    path('v1/courses/by-tutor/<uuid:owner_uuid>/<uuid:course_uuid>', CourseByTutorAPIView.as_view(
        {
         'delete': 'destroy'
        }),
         name="courses_by-tutor_api_delete"),
    path('v1/topics/by-courses/<uuid:course_uuid>', TopicByCourseAPIView.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    ), name="topic_by-course_api"),
    path('v1/topics/by-courses/<uuid:course_uuid>/<uuid:topic_uuid>', TopicByCourseAPIView.as_view(
        {
            'delete': 'destroy'
        }
    ), name="topic_by-course_delete_api"),
    path('v1/tasklist/by-topic/<uuid:topic_uuid>', TasklistByTopicAPIView.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    ), name="tasklist_by-topic_api"),
    path('v1/tasklist/by-topic/<uuid:topic_uuid>/<uuid:list_uuid>', TasklistByTopicAPIView.as_view(
        {
            'delete': 'destroy'
        }
    ), name="tasklist_by-topic_delete_api"),
    path('v1/task/by-tasklist/<uuid:list_uuid>', TaskByTaskListAPIView.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    ), name="task_by-tasklist_api"),
    path('v1/task/by-tasklist/<uuid:list_uuid>/<uuid:task_uuid>', TaskByTaskListAPIView.as_view(
        {
            'delete': 'destroy'
        }
    ), name="task_by-tasklist_delete_api")
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