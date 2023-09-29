from django.contrib import admin

from .models import StudentGroup, StudentGroupRelationship, TaskListGroupRelationship

admin.site.register(StudentGroup)
admin.site.register(StudentGroupRelationship)
admin.site.register(TaskListGroupRelationship)
