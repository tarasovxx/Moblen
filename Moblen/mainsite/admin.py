from django.contrib import admin
from .models import Course, Topic, TaskList, TaskListGroupRelationship, Task


# Регистрация моделей в административной панели
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(TaskList)
admin.site.register(TaskListGroupRelationship)
admin.site.register(Task)

