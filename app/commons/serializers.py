from rest_framework import serializers

class UuidSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True, source="uuid")

    class Meta:
        abstract = True
        exclude = ("uuid",)