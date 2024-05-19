"""
API Views for phishing module.
Swagger used for API documentation.
"""
from .attack import AttackAPIView
from .phishing_choices import PhishingChoicesAPIView

__all__ = (
    "AttackAPIView",
    "PhishingChoicesAPIView",
)
