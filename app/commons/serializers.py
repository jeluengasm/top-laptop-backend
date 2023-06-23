from rest_framework import serializers

class UuidSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, source="uuid")

    class Meta:
        abstract = True
        exclude = ("uuid",)