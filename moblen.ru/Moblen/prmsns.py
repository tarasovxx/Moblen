from rest_framework import permissions


class IsCurrentTutor(permissions.BasePermission):
    def has_permission(self, request, view):
        tutor_uuid = view.kwargs.get('tutor_uuid')
        if request.user.is_authenticated:
            return request.user.user_uuid == tutor_uuid
        return False


class IsCurrentStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        student_uuid = view.kwargs.get("student_uuid")
        if request.user.is_authenticated:
            return request.user.user_uuid == student_uuid
        return False
