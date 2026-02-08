from unica_api.email_sender import send_email
from unica_api.sms_sender import send_sms
from unica_api.call_sender import make_call


def trigger_campaign(customer_id, strategy, channel, customer_email=None, customer_phone=None):
    """
    Execute campaign via selected channel.
    Returns structured execution result.
    """

    message = f"We have a {strategy} campaign for you."

    channel_normalized = (channel or "").lower()

    # -----------------------------
    # Email Channel
    # -----------------------------
    if channel_normalized == "email":
        if not customer_email:
            return {
                "status": "failed",
                "channel": "email",
                "reason": "No email provided",
                "customer_id": customer_id
            }

        subject = f"{strategy} Campaign"

        result = send_email(customer_email, subject, message)

        return {
            "status": "email_sent",
            "channel": "email",
            "customer_id": customer_id,
            "email_result": result
        }

    # -----------------------------
    # SMS Channel
    # -----------------------------
    elif channel_normalized == "sms":
        if not customer_phone:
            return {
                "status": "failed",
                "channel": "sms",
                "reason": "No phone number provided",
                "customer_id": customer_id
            }

        result = send_sms(customer_phone, message)

        return {
            "status": "sms_sent",
            "channel": "sms",
            "customer_id": customer_id,
            "sms_result": result
        }

    # -----------------------------
    # Call Channel
    # -----------------------------
    elif channel_normalized == "call":
        if not customer_phone:
            return {
                "status": "failed",
                "channel": "call",
                "reason": "No phone number provided",
                "customer_id": customer_id
            }

        result = make_call(customer_phone, message)

        return {
            "status": "call_initiated",
            "channel": "call",
            "customer_id": customer_id,
            "call_result": result
        }

    # -----------------------------
    # Unsupported Channel
    # -----------------------------
    else:
        return {
            "status": "failed",
            "channel": channel,
            "reason": "Unsupported channel",
            "customer_id": customer_id
        }
