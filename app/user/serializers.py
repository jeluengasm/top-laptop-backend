from commons.serializers import UuidSerializer
from user.models import User


class UserSerializer(UuidSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'is_active')
        read_only_fields = ('id', 'email', 'is_active')