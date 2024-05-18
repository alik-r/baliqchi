from django.http import Http404
from django.shortcuts import get_object_or_404, render
from drf_yasg.utils import swagger_auto_schema

from attacks.phishing.models import Phishing
from core.models import Target
from core.repositories import incident_repository


@swagger_auto_schema(
    operation_description="Phishing page",
    tags=["Phishing"],
    responses={
        200: "Success",
        400: "Bad Request",
    },
)
def render_html(request, url):
    phishing_obj: Phishing = get_object_or_404(Phishing, url=url)
    template = str(phishing_obj.html).split("templates/")[1]

    query = request.GET.get('q')

    if query:
        try:
            target: Target = get_object_or_404(Target, pk=query)
            incident_repository.create(target=target, attack_type=("phishing", "Phishing",))
        except Http404:
            pass

    return render(request, template)
