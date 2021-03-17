from rest_framework import permissions


class IsNoteOwner(permissions.BasePermission):
    """пользователь является владельцем заметки"""

    message = 'Это не ваша заметка, идите лесом! =P.'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user