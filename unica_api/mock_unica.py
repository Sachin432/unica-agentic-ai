def trigger_campaign(customer_id, strategy, channel):
    return {
        "status": "triggered",
        "customer_id": customer_id,
        "strategy": strategy,
        "channel": channel
    }
