from uuid import uuid4

from rest_framework import viewsets

class ModelViewSet(viewsets.ModelViewSet):
    lookup_field = "uuid"

    class Meta:
        abstract = True

class ReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "uuid"

    class Meta:
        abstract = True