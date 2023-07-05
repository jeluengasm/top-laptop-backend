from rest_access_policy import AccessPolicy
from user.models import Role


class AccessPolicy(AccessPolicy):
    def role_must_be(self, request, view, action, field):
        if request.user.is_superuser:
            return True
        try:
            request.user.roles.get(slug=field)
            return True
        except Role.DoesNotExist:
            pass
        return False

    @classmethod
    def scope_queryset(cls, request, queryset):
        return queryset
