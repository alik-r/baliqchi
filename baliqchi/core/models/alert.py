from django.db import models
from datetime import datetime

from .incident import Incident

def generate_timestamp():
    return int(datetime.now().timestamp() * 1000)

class Alert(models.Model):
    STATUS_CHOICES = [
        ('firing', 'Firing'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    labels = models.JSONField()
    annotations = models.JSONField()
    starts_at = models.DateTimeField()
    generator_url = models.CharField(max_length=255)
    fingerprint = models.CharField(max_length=255)
    timestamp = models.BigIntegerField(default=generate_timestamp)
    incident = models.OneToOneField(Incident, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Alert {self.fingerprint} {self.starts_at.isoformat()} ({self.status})"
