from django.db import models

from django_prometheus.models import ExportModelOperationsMixin

from core.tools import BaseModel


class Target(ExportModelOperationsMixin('target'), BaseModel):
    """
    Model representing a target.

    Inherits from:
    - ExportModelOperationsMixin: Mixin for exporting model operations to Prometheus.
    - BaseModel: Base model for all models in the application.

    Attributes:
    - phone_number: Char field for the phone number of the target.
    - device_info: Char field for additional information about the target's device.
    """
    phone_number = models.CharField(max_length=15)
    device_info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.phone_number
