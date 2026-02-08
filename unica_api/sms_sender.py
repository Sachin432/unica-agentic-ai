import os
from twilio.rest import Client

def send_sms(to_phone, message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_phone = os.getenv("TWILIO_PHONE_NUMBER")

    if not all([account_sid, auth_token, from_phone]):
        return {"status": "failed", "reason": "Twilio credentials not configured"}

    client = Client(account_sid, auth_token)

    msg = client.messages.create(
        to=to_phone,
        from_=from_phone,
        body=message
    )

    return {
        "status": "sms_sent",
        "sid": msg.sid,
        "to": to_phone
    }
