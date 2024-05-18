from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def incident_callback(request):
    if request.method == 'POST':
        # TODO: Handle incident callback
        return JsonResponse({'status': 'incident_callback received'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def alertmanager_webhook(request):
    if request.method == 'POST':
        alert_data = json.loads(request.body)
        print(alert_data)
        return JsonResponse({'status': 'alert received'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
