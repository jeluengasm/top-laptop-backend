from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from user.managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_("email"), unique=True, max_length=255
    )
    name = models.CharField(_("name"), max_length=255, blank=True)
    roles = models.ManyToManyField(
        "user.Role", verbose_name=_("roles"), blank=True
    )
    is_active = models.BooleanField(verbose_name=_("active"), default=True)
    is_staff = models.BooleanField(verbose_name=_("staff"), default=False)
    registered_at = models.DateTimeField(
        verbose_name=_("registered at"), auto_now_add=timezone.now
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"), auto_now=True
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    objects = UserManager()


class Role(models.Model):
    name = models.CharField(_("name"), max_length=255)
    slug = models.SlugField(_("slug"), unique=True)

    def __str__(self):
        return self.name