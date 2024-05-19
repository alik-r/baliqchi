from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

@csrf_exempt
def incident_callback(request):
    if request.method == 'POST':
        # TODO: Handle incident callback
        incident_data = json.loads(request.body) if request.body else {}
        incident_str = json.dumps(incident_data, indent=None)
        logger.info(f"Incident recorded: {incident_str}")
        return JsonResponse({'status': 'Incident recorded.'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def alertmanager_webhook(request):
    if request.method == 'POST':
        alert_data = json.loads(request.body)
        alert_str = json.dumps(alert_data, indent=None)
        ts = datetime.now().timestamp()
        logger.info(f"ts={ts} alert_data={alert_str}")
        return JsonResponse({'status': 'alert received'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
