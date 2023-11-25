from uuid import UUID
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import View, Request


class CheckinPermissionChecker(BasePermission): 
    def has_permission(self, request: Request, view: View) -> bool:
        if request.user.is_authenticated and request.user.is_superuser and request.method in SAFE_METHODS:
            return True
        
        try:
            return request.user.is_authenticated and request.user.id == UUID(request.data.get('employee_id', None))
        except (Exception):
            return False
