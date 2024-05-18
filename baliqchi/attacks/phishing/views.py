from django.http import HttpResponse


def send_msg(request):
    # from baliqchi.settings import twilio_client, TWILIO_PHONE_NUMBER

    # message = twilio_client.messages \
    #     .create(
    #         body="Salam A kishi",
    #         from_=TWILIO_PHONE_NUMBER,
    #         to="+994XXXYYZZ"
    #     )

    return HttpResponse("Success")
