import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


def normalize_phone(phone):
    """
    Convert phone number to E.164 format.
    Example: 6299442449 -> +916299442449
    """
    phone = str(phone).strip()

    if phone.startswith("+"):
        return phone

    # Default to India country code
    return "+91" + phone


def make_call(to_phone, message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_phone = os.getenv("TWILIO_PHONE_NUMBER")

    if not all([account_sid, auth_token, from_phone]):
        return {
            "status": "failed",
            "channel": "call",
            "reason": "Twilio credentials not configured"
        }

    if not to_phone:
        return {
            "status": "failed",
            "channel": "call",
            "reason": "No destination phone number provided"
        }

    try:
        client = Client(account_sid, auth_token)

        to_number = normalize_phone(to_phone)

        # Twilio requires TwiML for calls
        twiml = f"""
<Response>
    <Say voice="alice">{message}</Say>
</Response>
"""

        call = client.calls.create(
            to=to_number,
            from_=from_phone,
            twiml=twiml
        )

        return {
            "status": "call_initiated",
            "channel": "call",
            "to": to_number,
            "sid": call.sid
        }

    except TwilioRestException as e:
        return {
            "status": "failed",
            "channel": "call",
            "reason": str(e)
        }
    except Exception as e:
        return {
            "status": "failed",
            "channel": "call",
            "reason": f"Unexpected error: {str(e)}"
        }
