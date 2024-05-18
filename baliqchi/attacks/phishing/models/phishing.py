from django.db import models

from core.models import BaseAttack


class Phishing(BaseAttack):
    message = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
