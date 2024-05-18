from django.db import models

from baliqchi.core.models import BaseModel


class BaseAttack(BaseModel):
    STATUSES = (
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('completed', 'Completed'),
    )
    title = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
    sent_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUSES, default='pending')

    # targets = models

    def __str__(self):
        return self.title
