from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from core.models.alert import Alert
from core.models.incident import Incident

@receiver(post_save, sender=Incident)
def incident_post_save(sender, instance, created, **kwargs):
    if created:
        data = {
            "incident_id": str(instance.id),
            "incident_created_at": instance.created_at.isoformat(),
            "attack_type": instance.attack_type,
            "target_number": instance.target.phone_number,
            "target_device_info": instance.target.device_info,
        }
        headers = {'Content-Type': 'application/json'}
        requests.post(f"{settings.BASE_URL}/incident-callback/", json=data, headers=headers)
    
    if instance.acknowledged:
        Alert.objects.filter(incident=instance).update(status="closed")