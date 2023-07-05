from django.contrib import admin
from user.models import User, Role
from user.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'name',
        'email',
        'is_active',
        'is_staff',
        'get_groups',
        'get_roles',
        'registered_at',
        'updated_at',
    )
    list_filter = ('is_active', 'is_staff', 'registered_at', 'updated_at')
    search_fields = ('email', 'name')
    ordering = ('name',)
    form = UserChangeForm
    add_form = UserCreationForm

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('name', 'email', 'password1', 'password2'),
            },
        ),
    )
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        (None, {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (None, {'fields': ('registered_at', 'updated_at')}),
        (None, {'fields': ('roles', 'groups')}),
    )
    readonly_fields = ('registered_at', 'updated_at')
    filter_horizontal = ('roles', 'groups')

    @admin.display(description='Groups')
    def get_groups(self, obj):
        return ', '.join([str(group) for group in obj.groups.all()])

    @admin.display(description='Roles')
    def get_roles(self, obj):
        return ', '.join([str(role) for role in obj.roles.all()])


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name',)
