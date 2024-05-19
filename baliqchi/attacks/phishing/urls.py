from django.urls import path
from attacks.phishing.api import *
from attacks.phishing import views
from attacks.phishing.phishing_page import phishing_page_view, attack_view

urlpatterns = [
    path("make-attack/", AttackAPIView.as_view(), name="make-attack"),
    path("phishing-choices/", PhishingChoicesAPIView.as_view(), name="phishing-choices"),
    path("phishing-page/<str:url>/u", phishing_page_view, name="phishing_page"),
    path("incident-callback/", views.incident_callback, name="incident-callback"),
    path("alerts/webhook/", views.webhook_receiver, name="alertmanager-webhook"),
    path("attack/", attack_view, name="attack-page"),
]
