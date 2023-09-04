from django.contrib import admin
from .models import Tutor, Student, StudentTutorRelationship, StudentGroup, StudentGroupRelationship


# Register your models here.
class TutorAdmin(admin.ModelAdmin):
    list_display = ('tutor_name', 'tutor_surname', 'phone_number', 'email', 'has_access')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_surname', 'phone_number', 'email')


admin.site.register(Tutor, TutorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentTutorRelationship)
admin.site.register(StudentGroup)
admin.site.register(StudentGroupRelationship)
