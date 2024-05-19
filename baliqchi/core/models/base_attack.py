from django.db import models
from core.tools import BaseModel


class BaseAttack(BaseModel):
    STATUSES = (
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('completed', 'Completed'),
    )
    title = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUSES, default='pending')

    def __str__(self):
        return self.title
