from django.db import models

from django_prometheus.models import ExportModelOperationsMixin

from core.tools import BaseModel

ATTACKS = (
    ("phishing", "Phishing"),
)


class Incident(ExportModelOperationsMixin('incident'), BaseModel):
    """
    Model representing an incident.

    Inherits from:
    - ExportModelOperationsMixin: Mixin for exporting model operations to Prometheus.
    - BaseModel: Base model for all models in the application.

    Attributes:
    - target: Foreign key linking to the Target model.
    - attack_type: Char field for the type of attack associated with the incident.
    - acknowledged: Boolean field indicating whether the incident has been acknowledged.
    """
    target = models.ForeignKey(
        "core.Target",
        related_name="incidents",
        verbose_name="Target",
        on_delete=models.SET_NULL,
        null=True,
    )
    attack_type = models.CharField(max_length=255, choices=ATTACKS, default=None)
    acknowledged = models.BooleanField(default=False)
