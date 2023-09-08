from django.contrib import admin
from .models import Course, Topic, TaskList, TaskListGroupRelationship, Task, ReferralLink


# Регистрация моделей в административной панели
class ReferralLinkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(TaskList)
admin.site.register(TaskListGroupRelationship)
admin.site.register(Task)
admin.site.register(ReferralLink, ReferralLinkAdmin)
