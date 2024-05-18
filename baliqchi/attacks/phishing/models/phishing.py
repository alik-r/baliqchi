from uuid import uuid4

from django.db import models

from core.models import BaseAttack

from django_prometheus.models import ExportModelOperationsMixin


class Phishing(ExportModelOperationsMixin('phishing'), BaseAttack):
    message = models.TextField()
    url = models.CharField(max_length=255)
    html = models.FileField(upload_to=f"baliqchi/attacks/phishing/templates/phishing/{uuid4()}/", blank=True)

    def __str__(self):
        return self.title
