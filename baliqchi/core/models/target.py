from django.db import models

from django_prometheus.models import ExportModelOperationsMixin

from core.tools import BaseModel


class Target(ExportModelOperationsMixin('target'), BaseModel):
    phone_number = models.CharField(max_length=15)
    device_info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.phone_number
