from commons.policies import AccessPolicy


class UserAccessPolicy(AccessPolicy):
    statements = [
        {
            'action': ['list', 'retrieve', 'profile'],
            'principal': ['authenticated'],
            'effect': 'allow',
        },
        {'action': ['login', 'logout'], 'principal': '*', 'effect': 'allow'},
    ]

    @classmethod
    def scope_queryset(cls, request, queryset):
        roles = {role.slug for role in request.user.roles.all()}
        if (
            getattr(request.user, 'is_staff')
            or getattr(request.user, 'is_superuser')
            or {'admin', 'data-analyst'} & roles
        ):
            return queryset
        elif {'agent', 'client'} & roles:
            return queryset.filter(pk=request.user.id, is_active=True)

        return queryset.none()
