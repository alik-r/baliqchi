from django.db import models

from django_prometheus.models import ExportModelOperationsMixin

from core.tools import BaseModel

ATTACKS = (
    ("phishing", "Phishing"),
)


class Incident(ExportModelOperationsMixin('incident'), BaseModel):
    target = models.ForeignKey(
        "core.Target",
        related_name="incidents",
        verbose_name="Target",
        on_delete=models.SET_NULL,
        null=True,
    )
    attack_type = models.CharField(max_length=255, choices=ATTACKS, default=None)
