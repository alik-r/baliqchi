from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from datetime import datetime

from core.models.incident import Incident
from core.models.alert import Alert

logger = logging.getLogger(__name__)

@csrf_exempt
def incident_callback(request):
    if request.method == 'POST':
        incident_data = json.loads(request.body) if request.body else {}
        incident_str = json.dumps(incident_data, indent=None)
        logger.info(f"Incident recorded: {incident_str}")
        return JsonResponse({'status': 'Incident recorded.'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def webhook_receiver(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        alert_str = json.dumps(data, indent=None)

        for alert_data in data.get('alerts', []):
            status = alert_data['status']
            labels = alert_data['labels']
            annotations = alert_data['annotations']
            starts_at = datetime.fromisoformat(alert_data['startsAt'].replace('Z', '+00:00'))
            generator_url = alert_data['generatorURL']
            fingerprint = alert_data['fingerprint']
            
            alert, created = Alert.objects.get_or_create(
                fingerprint=fingerprint,
                defaults={
                    'status': status,
                    'labels': labels,
                    'annotations': annotations,
                    'starts_at': starts_at,
                    'generator_url': generator_url,
                    'incident': Incident.objects.latest('created_at')
                }
            )

            if alert.status == "closed":
                return JsonResponse({"status": "Closed alert"}, status=200)

            if not created:
                alert.status = status if alert.status != "closed" else status
                alert.labels = labels
                alert.annotations = annotations
                alert.starts_at = starts_at
                alert.generator_url = generator_url
                alert.save()

        logger.info(f"ts={alert.timestamp} alert_data={alert_str}")
        return JsonResponse({"status": "success"}, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)