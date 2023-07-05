from commons.serializers import UuidSerializer
from dashboards import models
from user.serializers import UserSerializer
from rest_framework import serializers
from user.models import User


class DashboardListSerializer(UuidSerializer):
    last_modified_by = serializers.SlugRelatedField(
        slug_field="name", queryset=User.objects.all(), required=False
    )
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = models.Dashboard
        exclude = ('uuid',)

    def validate(self, attrs):
        if (
            self.context['action'] in ('create', 'update', 'partial_update')
            and attrs.get('last_modified_by') is None
        ):
            attrs['last_modified_by'] = self.context['request'].user
        return attrs


class DashboardDetailSerializer(UuidSerializer):
    last_modified_by = UserSerializer()

    class Meta:
        model = models.Dashboard
        exclude = ('uuid',)


class LaptopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Laptops
        fields = '__all__'
