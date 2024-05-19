from rest_framework import serializers

from attacks.phishing.tools import get_phishing_choices


class PhishingAttackSerializer(serializers.Serializer):
    """
    Serializer for conducting phishing attacks.

    Attributes:
    - phishing_model: Choice field for selecting a phishing method.
    """
    phishing_model = serializers.ChoiceField(choices=get_phishing_choices())
