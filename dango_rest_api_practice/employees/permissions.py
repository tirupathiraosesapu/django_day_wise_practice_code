from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "ADMIN"


class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [
            "ADMIN",
            "MANAGER",
        ]


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ["SUPER_ADMIN", "ADMIN"]:
            return True
        return obj.user == request.user
