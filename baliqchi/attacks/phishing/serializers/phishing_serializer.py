from rest_framework import serializers

from attacks.phishing.tools import get_phishing_choices


class PhishingAttackSerializer(serializers.Serializer):
    phishing_model = serializers.ChoiceField(choices=get_phishing_choices())
