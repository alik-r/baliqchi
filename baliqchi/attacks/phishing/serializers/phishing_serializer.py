from enum import Enum
from typing import List

from django.db.models import QuerySet
from rest_framework import serializers

from attacks.phishing.models import Phishing


class PhishingAttackSerializer(serializers.Serializer):
    phishing_queryset: QuerySet = Phishing.objects.values("id", "title")
    phishing_choices = tuple(map(lambda x: (x["id"], x["title"],), phishing_queryset))

    phishing_model = serializers.ChoiceField(choices=phishing_choices)
