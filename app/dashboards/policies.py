from commons.policies import AccessPolicy


class DashBoardManagerPolicy(AccessPolicy):
    statements = [
        {
            'action': ['*'],
            'principal': ['group:admin', 'group:data', 'admin'],
            'effect': 'allow',
            'condition_expression': 'role_must_be:admin or role_must_be:data-analyst',
        }
    ]

    @classmethod
    def scope_queryset(cls, request, queryset):
        roles = {role.slug for role in request.user.roles.all()}
        if (getattr(request.user, 'is_staff') 
            or getattr(request.user, 'is_superuser') 
            or {'admin', 'data-analyst'} & roles):
            return queryset

        return queryset.none()


class LaptopsPolicy(AccessPolicy):
    statements = [
        {
            'action': ['*'],
            'principal': ['group:admin', 'group:data', 'admin'],
            'effect': 'allow',
        }
    ]