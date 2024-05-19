from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models.alert import Alert
from core.models.incident import Incident

@receiver(post_save, sender=Incident)
def incident_post_save(sender, instance, created, **kwargs):
    if created:
        return
    
    if instance.acknowledged:
        Alert.objects.filter(incident=instance).update(status="closed")