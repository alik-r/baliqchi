from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    """
    Base model for all models in the application.

    Attributes:
    - id: UUID field for the primary key.
    - created_at: DateTime field for the creation timestamp.
    - updated_at: DateTime field for the last update timestamp.
    - is_deleted: Boolean field indicating whether the model is deleted.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
