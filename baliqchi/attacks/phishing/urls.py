from django.urls import path
from attacks.phishing.api import *

urlpatterns = [
    path("test/", test_view, name="test-view"),
    path("make-attack", AttackAPIView.as_view(), name="make-attack")
]
