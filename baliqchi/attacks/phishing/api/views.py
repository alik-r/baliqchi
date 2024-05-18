from typing import List

from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from attacks.phishing.serializers import PhishingAttackSerializer
from attacks.phishing.tools.sms_sender import initialize_attack
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


def test_view(request):
    # get_choices()

    return HttpResponse("Success")
