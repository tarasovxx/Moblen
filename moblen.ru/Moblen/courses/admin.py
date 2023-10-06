from django.contrib import admin
from .models import Course, Topic, Task, TaskList

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_uuid', 'owner_uuid', 'course_name')
    search_fields = ('curse_name',)
    list_display_links = ('owner_uuid',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_uuid', 'list_uuid', 'task_condition', 'task_image', 'task_answer', 'criteria')
    search_fields = ('task_condition',)
    list_display_links = ('list_uuid',)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_uuid', 'course_uuid', 'topic_name')
    search_fields = ['topic_name']
    list_display_links = ['course_uuid']

class TaskListAdmin(admin.ModelAdmin):
    list_display = ('list_uuid', 'topic_uuid', 'list_name')
    search_fields = ['list_name']
    list_display_links = ['topic_uuid']




# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin)