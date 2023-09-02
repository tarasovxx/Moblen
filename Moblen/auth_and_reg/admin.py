from django.contrib import admin
from .models import Tutor, Student, StudentTutorRelationship, StudentGroup, StudentGroupRelationship

# Register your models here.
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(StudentTutorRelationship)
admin.site.register(StudentGroup)
admin.site.register(StudentGroupRelationship)