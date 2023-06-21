from django.contrib.auth.models import BaseUserManager, Group
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email,password, is_staff, is_superuser, groups=None, roles=None, is_active=True, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=timezone.now(),
            registered_at=timezone.now(),
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        if groups:
            for group in groups:
                user.groups.add(Group.objects.get(name=group))

        if roles:
            for role in roles:
                user.roles.add(role)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, groups=None, roles=None, is_active=True, **extra_fields):
        is_staff = extra_fields.pop('is_staff', False)
        is_superuser = extra_fields.pop('is_superuser', False)
        return self._create_user(email, password, is_staff, is_superuser, groups, roles, is_active, **extra_fields,)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )
