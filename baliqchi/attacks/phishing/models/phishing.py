from uuid import uuid4

from django.db import models

from core.models import BaseAttack

from django_prometheus.models import ExportModelOperationsMixin


class Phishing(ExportModelOperationsMixin('phishing'), BaseAttack):
    """
    Model representing a phishing attack.

    Inherits from:
    - ExportModelOperationsMixin: Mixin for exporting model operations to Prometheus.
    - BaseAttack: Base model for all attack types.

    Attributes:
    - message: Text field for the message of the phishing attack.
    - url: Char field for the URL associated with the phishing attack.
    - html: File field for the HTML content of the phishing page.
    """
    message = models.TextField()
    url = models.CharField(max_length=255)
    html = models.FileField(upload_to=f"baliqchi/attacks/phishing/templates/phishing/{uuid4()}/", blank=True)

    def __str__(self):
        return self.title
