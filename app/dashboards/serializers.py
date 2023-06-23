from commons.serializers import UuidSerializer
from dashboards import models
from user.serializers import UserSerializer
from rest_framework import serializers
from user.models import User

class DashboardListSerializer(UuidSerializer):
    last_modified_by = serializers.SlugRelatedField(
        slug_field="uuid", queryset=User.objects.all()
    )
    class Meta:
        model = models.Dashboard
        exclude = ('uuid', 'created_at', 'updated_at')


class DashboardDetailSerializer(UuidSerializer):
    last_modified_by = UserSerializer()

    class Meta:
        model = models.Dashboard
        exclude = ('uuid', 'created_at', 'updated_at')


class LaptopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Laptops
        fields = '__all__'
