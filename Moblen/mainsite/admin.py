from django.contrib import admin
from .models import Tutor, Student, StudentTutorRelationship, StudentGroup, StudentGroupRelationship, \
    Course, Topic, TaskList, TaskListGroupRelationship, Task

# Регистрация моделей в административной панели
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(StudentTutorRelationship)
admin.site.register(StudentGroup)
admin.site.register(StudentGroupRelationship)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(TaskList)
admin.site.register(TaskListGroupRelationship)
admin.site.register(Task)
