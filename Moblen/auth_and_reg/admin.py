from django.contrib import admin
from .models import Tutor, Student, StudentTutorRelationship, StudentGroup, StudentGroupRelationship


# Register your models here.
class TutorAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'tutor_name', 'tutor_surname', 'has_access')
    search_fields = ('phone_number', 'email')
    list_display_links = ('phone_number', 'email')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'student_name', 'student_surname')
    search_fields = ('phone_number', 'email')
    list_display_links = ('phone_number', 'email')


class StudentGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tutor, TutorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentTutorRelationship)
admin.site.register(StudentGroup, StudentGroupAdmin)
admin.site.register(StudentGroupRelationship)
