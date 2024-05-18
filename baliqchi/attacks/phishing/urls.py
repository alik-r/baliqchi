from django.urls import path
from attacks.phishing.api import *
from attacks.phishing import views

urlpatterns = [
    path("test/", test_view, name="test-view"),
    path("make-attack/", AttackAPIView.as_view(), name="make-attack"),
    path("phishing-choices/", PhishingChoicesAPIView.as_view(), name="phishing-choices"),
    path("phishing-page/<str:url>/u", render_html, name="phishing_page"),
    path("incident-callback/", views.incident_callback, name="incident-callback"),
    path("alerts/webhook/", views.alertmanager_webhook, name="alertmanager-webhook"),
]
