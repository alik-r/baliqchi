from django.urls import path
import attacks.phishing.views as views

urlpatterns = [
    path("test/", views.test_view, name="test-view"),
    path("make-attack", views.AttackAPIView.as_view(), name="make-attack")
]
