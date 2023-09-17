from django.urls import path
from .models import Course, Topic, Task, TaskList
from .api import CourseAPIView, CourseDetailAPIView, TopicAPIView, TopicDetailAPIView, TaskListAPIView, \
    TaskListDetailAPIView, TaskAPIView, TaskDetailAPIView, CourseTutorAPIView

urlpatterns = [
    path('v1/courses/', CourseAPIView.as_view(
        {'get': 'list',
         'post': 'create'}),
         name="all_courses_api"),
    path('v1/courses/<uuid:tutor_uuid>/from-the-tutor/', CourseTutorAPIView.as_view(
        {'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'}),
         name="courses_api"),
    path('v1/topic/', TopicAPIView.as_view(
        {'post': 'create'}),
         name="all_topics_api"),
    path('v1/topic/<uuid:courses_uuid>/in-the-courses', TopicDetailAPIView.as_view(
        {'get': 'retrieve',
        'patch': 'partial_update',
         'delete': 'destroy'}),
         name="topic_api"),
    path('v1/tasklist/', TaskListAPIView.as_view(
        {'post': 'create'}),
         name="all_tasklist_api"),
    path('v1/tasklist/<uuid:topic_uuid>/in-the-topic/', TaskListDetailAPIView.as_view(
        {'get': 'retrieve',
         'patch': 'partial_update',
         'delete': 'destroy'}),
         name="courses_api"),
    path('v1/task/', TaskAPIView.as_view(
        {'post': 'create'}),
         name="all_tasks_api"),
    path('v1/task/<uuid:tasklist_uuid>/in-the-task-list', TaskDetailAPIView.as_view(
        {'get': 'retrieve',
         'patch': 'partial_update',
         'delete': 'destroy'}),
         name="task_api")
]