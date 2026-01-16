def governance_agent(customer, campaign):
    if customer["opt_out"]:
        return False, "Customer opted out"
    if customer["fatigue_score"] > 0.8:
        return False, "Over-messaging risk"
    return True, "Approved"
