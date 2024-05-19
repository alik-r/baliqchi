from django.http import Http404
from django.shortcuts import get_object_or_404, render

from attacks.phishing.models import Phishing
from attacks.phishing.tools import get_phishing_choices
from baliqchi.settings import BASE_URL
from core.models import Target
from core.repositories import incident_repository


def phishing_page_view(request, url):
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


def attack_view(request):
    return render(
        request,
        template_name="phishing/phishing.html",
        context={
            "red_button": f"{BASE_URL}/make-attack",  # endpoint url for starting attack
            "choices": get_phishing_choices(),
        }
    )
