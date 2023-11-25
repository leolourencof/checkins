from uuid import UUID
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import View, Request


class UserPermissionChecker(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        try:
            user_id_param = UUID(str(view.kwargs.get('pk', None)))
            return request.user.is_authenticated and request.method in SAFE_METHODS and user_id_param == request.user.id
        except(Exception):
            return False
