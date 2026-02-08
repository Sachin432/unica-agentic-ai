import os
from twilio.rest import Client

def make_call(to_phone, message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_phone = os.getenv("TWILIO_PHONE_NUMBER")

    if not all([account_sid, auth_token, from_phone]):
        return {"status": "failed", "reason": "Twilio credentials not configured"}

    client = Client(account_sid, auth_token)

    # Twilio needs a TwiML URL or TwiML instructions.
    # We can use Twilio's demo echo or say a message using TwiML.
    twiml = f"""
    <Response>
        <Say voice="alice">{message}</Say>
    </Response>
    """

    call = client.calls.create(
        to=to_phone,
        from_=from_phone,
        twiml=twiml
    )

    return {
        "status": "call_initiated",
        "sid": call.sid,
        "to": to_phone
    }
