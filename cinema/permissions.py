from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        if (request.method in SAFE_METHODS
                and (request.user and request.user.is_authenticated)):
            return True
        return False


class ActionPermission(BasePermission):

    allowed_actions = []

    def has_permission(self, request, view):
        if not self.allowed_actions:
            return True
        return view.action in self.allowed_actions


class ListCreatePermission(ActionPermission):
    allowed_actions = ["GET", "POST"]


class ListCreateRetrievePermission(ActionPermission):
    allowed_actions = ["GET", "POST"]


class AllPermission(ActionPermission):
    allowed_actions = ["GET", "POST", "PUT", "PATCH", "DELETE"]
