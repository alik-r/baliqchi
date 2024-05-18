from uuid import uuid4

from django.db import models

from baliqchi.attacks import ATTACKS


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Target(BaseModel):
    phone_number = models.CharField(max_length=15)
    clicked = models.BooleanField(default=False)
    click_timestamp = models.DateTimeField(null=True, blank=True)
    device_info = models.CharField(max_length=255, null=True, blank=True)
    # organization = models.CharField(max_length=255, null=True, blank=True)  # Organization

    def __str__(self):
        return self.phone_number


class Incident(BaseModel):
    target = models.ForeignKey(
        "core.Target",
        related_name="incidents",
        verbose_name="Incidents",
        on_delete=models.SET_NULL,
    )
    attack_type = models.CharField(max_length=255, choices=ATTACKS, default=None)
    