from django.db import models

from core.models import BaseAttack

from django_prometheus.models import ExportModelOperationsMixin


class Phishing(ExportModelOperationsMixin('phishing'), BaseAttack):
    message = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
