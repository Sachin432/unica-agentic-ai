from agents.customer_agent import customer_agent
from agents.strategy_agent import strategy_agent
from agents.channel_agent import channel_agent
from agents.governance_agent import governance_agent


def run_orchestration(llm, customer: dict) -> dict:
    """
    End-to-end autonomous campaign orchestration.
    Returns clean, flat, execution-ready output.
    """

    # -----------------------------
    # 1. Customer Insight Agent
    # -----------------------------
    insight = customer_agent(llm, customer)

    # -----------------------------
    # 2. Strategy Decision Agent
    # -----------------------------
    strategy_result = strategy_agent(llm, insight)
    strategy = strategy_result.get("strategy", "DoNothing")

    # -----------------------------
    # 3. Channel Decision Agent
    # -----------------------------
    channel_result = channel_agent(llm, strategy)
    channel = channel_result.get("channel", "Email")
    send_time = channel_result.get("send_time", "Weekday morning")

    # -----------------------------
    # 4. Governance Agent
    # -----------------------------
    approved, governance_reason = governance_agent(customer, strategy)

    # -----------------------------
    # 5. Final Orchestration Output
    # -----------------------------
    return {
        # Reasoning (for UI / audit)
        "insight": insight,

        # Decisions (for execution)
        "strategy": strategy,
        "channel": channel,
        "send_time": send_time,

        # Governance
        "approved": approved,
        "governance_reason": governance_reason
    }
