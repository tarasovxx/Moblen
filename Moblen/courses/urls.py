from django.urls import path
from .models import Course, Topic, Task, TaskList
from .views import CourseAPIView, CourseDetailAPIView, TopicAPIView, TopicDetailAPIView, TaskListAPIView, \
    TaskListDetailAPIView, TaskAPIView, TaskDetailAPIView, CourseTutorAPIView

urlpatterns = [
    path('v1/courses/', CourseAPIView.as_view({'post': 'create'}), name="all_courses_api"),
    path('v1/courses/<uuid:tutor_uuid>/', CourseTutorAPIView.as_view({'get': 'retrieve',
                                                                    'patch': 'partial_update',
                                                                    'delete': 'destroy'
                                                                    }), name="courses_api"),
    path('v1/courses/<uuid:course_uuid>/', CourseDetailAPIView.as_view({'get': 'retrieve',
                                                                    'patch': 'partial_update',
                                                                    'delete': 'destroy'
                                                                    }), name="courses_api"),
    path('v1/topic/', TopicAPIView.as_view({'post': 'create'}), name="all_topics_api"),
    path('v1/topic/<uuid:topic_uuid>/', TopicDetailAPIView.as_view({'get': 'retrieve',
                                                                          'patch': 'partial_update',
                                                                          'delete': 'destroy'
                                                                          }), name="topic_api"),
    path('v1/tasklist/', TaskListAPIView.as_view({'post': 'create'}), name="all_tasklist_api"),
    path('v1/tasklist/<uuid:tasklist_uuid>/', TaskListDetailAPIView.as_view({'get': 'retrieve',
                                                                        'patch': 'partial_update',
                                                                        'delete': 'destroy'
                                                                        }), name="courses_api"),
    path('v1/task/', TaskAPIView.as_view({'post': 'create'}), name="all_tasks_api"),
    path('v1/task/<uuid:task_uuid>/', TaskDetailAPIView.as_view({'get': 'retrieve',
                                                                    'patch': 'partial_update',
                                                                    'delete': 'destroy'
                                                                    }), name="task_api")
]