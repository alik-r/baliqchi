from django.db.models import QuerySet

from attacks.phishing.models import Phishing


def get_phishing_choices():
    phishing_queryset: QuerySet = Phishing.objects.values("id", "title")
    phishing_choices = tuple(map(lambda x: (x["id"], x["title"],), phishing_queryset))

    return phishing_choices
