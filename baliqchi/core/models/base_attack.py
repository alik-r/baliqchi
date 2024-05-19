from django.db import models
from core.tools import BaseModel


class BaseAttack(BaseModel):
    """
    Base model for all attack types.

    Attributes:
    - STATUSES: Choices for the status of the attack.
    - title: Char field for the title of the attack.
    - scheduled_time: DateTime field for the scheduled time of the attack.
    - status: Char field for the status of the attack.
    """
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
