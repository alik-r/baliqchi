from typing import Tuple

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from attacks.phishing.tools import get_phishing_choices
from core.tools import response


class PhishingChoicesAPIView(APIView):
    """
    API endpoint to retrieve the available phishing methods.
    """
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_description="Get enum of available phishing methods",
        tags=["Phishing"],
        responses={
            201: openapi.Response(
                description="Choices"
            ),
            400: "Bad Request",
        },
    )
    def get(self, request):
        try:
            choices: Tuple[AllowAny] = get_phishing_choices()
            return response.Ok(
                {
                    "detail": "Phishing Choices",
                    "data": choices,
                }
            )
        except Exception as e:
            print(e)
            return response.InternalServerError("Server error")
