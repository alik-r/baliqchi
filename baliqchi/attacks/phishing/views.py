import re
from typing import List

from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from attacks.phishing.models import Phishing
from attacks.phishing.serializers import PhishingAttackSerializer
from core.models import Target
from core.tools import response


class AttackAPIView(APIView):
    serializer_class = PhishingAttackSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_description="Attack on targets",
        request_body=PhishingAttackSerializer,
        tags=["Attack"],
        responses={
            201: openapi.Response(
                description="Attacks are being executed."
            ),
            400: "Bad Request",
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            targets: List[Target] | None = get_list_or_404(Target)
            phishing_id: str = serializer.validated_data["phishing_model"]
            results = list(map(initialize_attack(phishing_id=phishing_id), targets))

            return response.Ok(
                {
                    "data": "Attacks are being executed."
                }
            )

        return response.BadRequest(serializer.errors)


def initialize_attack(phishing_id: str):
    phishing_model: Phishing = get_object_or_404(Phishing, pk=phishing_id)
    body: str = phishing_model.message
    url: str = f"{(url := phishing_model.url)}{("/" if url[-1] != "/" else "")}?q="

    def send_phishing(target: Target):
        target_number: str = target.phone_number
        final_url: str = f"{url}{target.id}"
        final_body: str = body.replace("{url}", final_url)

        send_msg(target=target_number, body=final_body)
        return "Success"

    return send_phishing


def send_msg(target: str, body: str):
    print(f"{target}:{body}")
    pass
    # from baliqchi.settings import twilio_client, TWILIO_PHONE_NUMBER

    # message = twilio_client.messages \
    #     .create(
    #         body=body,
    #         from_=TWILIO_PHONE_NUMBER,
    #         to=target
    #     )


def test_view(request):
    # get_choices()

    return HttpResponse("Success")
