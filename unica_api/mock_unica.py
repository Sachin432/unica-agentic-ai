from unica_api.email_sender import send_email

def trigger_campaign(customer_id, strategy, channel, customer_email=None):
    # In real Unica, this would trigger journeys/campaigns

    if channel.lower() == "email":
        if not customer_email:
            return {"status": "failed", "reason": "No email provided"}

        subject = f"{strategy} Campaign for You"
        body = f"""
Hello,

We have a special {strategy} campaign tailored for you.

Thank you,
Marketing Team
"""
        result = send_email(customer_email, subject, body)
        return {
            "status": "triggered",
            "channel": "Email",
            "customer_id": customer_id,
            "email_result": result
        }

    elif channel.lower() == "sms":
        return {"status": "triggered", "channel": "SMS", "customer_id": customer_id}

    elif channel.lower() == "push":
        return {"status": "triggered", "channel": "Push", "customer_id": customer_id}

    else:
        return {"status": "failed", "reason": "Unknown channel"}
