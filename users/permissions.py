from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """Разрешение, которое позволяет доступ только активным сотрудникам."""

    def has_permission(self, request, view):
        # Проверяем, является ли пользователь активным сотрудником
        return request.user.is_active and request.user.is_staff
