from unica_api.email_sender import send_email
from unica_api.sms_sender import send_sms
from unica_api.call_sender import make_call

def trigger_campaign(customer_id, strategy, channel, customer_email=None, customer_phone=None):
    message = f"We have a {strategy} campaign for you."

    if channel.lower() == "email":
        if not customer_email:
            return {"status": "failed", "reason": "No email provided"}
        subject = f"{strategy} Campaign"
        return send_email(customer_email, subject, message)

    elif channel.lower() == "sms":
        if not customer_phone:
            return {"status": "failed", "reason": "No phone number provided"}
        return send_sms(customer_phone, message)

    elif channel.lower() == "call":
        if not customer_phone:
            return {"status": "failed", "reason": "No phone number provided"}
        return make_call(customer_phone, message)

    else:
        return {"status": "failed", "reason": "Unsupported channel"}
