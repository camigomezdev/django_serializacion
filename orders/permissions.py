

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.seller == request.user


class IsAdminandIsActiveUser(BasePermission):
    message = 'No puedes realizar esta acción porque no eres admin y/o estas activo'

    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS:
        #     return True
        # else:
        #     return (request.user
        #             and request.user.is_staff
        #             and request.user.is_active)

        return False
