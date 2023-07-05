from django.db import models
import uuid


class TokenBasedModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, db_index=True
    )

    class Meta:
        abstract = True
