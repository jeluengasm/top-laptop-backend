from django.contrib import admin
from user.models import User, Role


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'registered_at', 'updated_at')
    list_filter = ('is_active', 'is_staff', 'registered_at', 'updated_at')
    search_fields = ('email', 'name')
    ordering = ('email',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name',)