from commons.serializers import UuidSerializer
from user.models import User, Role
from django.contrib.auth.models import Group


class RoleSerializer(UuidSerializer):
    class Meta:
        model = Role
        fields = ('slug',)


class GroupSerializer(UuidSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(UuidSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'is_active')
        read_only_fields = ('id', 'email', 'is_active')


class UserProfileSerializer(UuidSerializer):
    roles = RoleSerializer(many=True)
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'is_active', 'roles', 'groups')
        read_only_fields = ('id', 'email', 'is_active', 'roles', 'groups')
