from django.shortcuts import get_object_or_404

from baliqchi.settings import twilio_client, TWILIO_PHONE_NUMBER
from baliqchi.settings import BASE_URL
from attacks.phishing.models import Phishing
from core.models import Target


def initialize_attack(phishing_id: str):
    """
    Function to initialize a phishing attack.

    Retrieves the phishing model corresponding to the provided ID,
    constructs the message body and URL, and sends the phishing message
    to the target.

    Parameters:
    - phishing_id: ID of the phishing model.

    Returns:
    - Function: Function to send phishing message to a target.
    """

    phishing_model: Phishing = get_object_or_404(Phishing, pk=phishing_id)
    body: str = phishing_model.message
    url: str = f"{(url := phishing_model.url)}{('/' if url[-1] != '/' else '')}"

    def send_phishing_message(target: Target):
        target_number: str = target.phone_number
        final_url: str = f"{BASE_URL}/test/phishing-page/{url}/u?q={target.id}"
        final_body: str = body.replace("{url}", final_url)

        send_msg(target=target_number, body=final_body)
        return "Success"

    return send_phishing_message


def send_msg(target: str, body: str):
    """
    Function to send a message using Twilio.

    Parameters:
    - target: Phone number of the recipient.
    - body: Body of the message.

    Returns:
    - None
    """
    message = twilio_client.messages \
        .create(
            body=body,
            from_=TWILIO_PHONE_NUMBER,
            to=target
        )
