import json
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def channel_agent(llm, strategy: str, customer: dict) -> dict:
    """
    Decide communication channel and send time based on strategy + customer signals.
    Returns structured output safe for orchestration.
    """

    prompt = PromptTemplate(
        input_variables=["strategy", "customer"],
        template="""
You are an enterprise marketing channel decision engine.

You are given:
1) Campaign strategy
2) Customer profile (JSON)

Your task:
- Choose EXACTLY ONE channel
- Choose a reasonable send time

ALLOWED CHANNELS:
- Email
- SMS
- Call

RULES:
- Prefer Email for highly engaged users
- Prefer SMS for medium engagement or quick nudges
- Prefer Call for low engagement or critical actions
- If customer has opt_out = true, still return a channel but governance may block later

IMPORTANT:
- Return ONLY valid JSON
- Do NOT add explanation
- Do NOT add markdown
- Do NOT add extra text

Return JSON in this EXACT format:
{{
  "channel": "<Email | SMS | Call>",
  "send_time": "<short description>"
}}

Campaign Strategy:
{strategy}

Customer Profile (JSON):
{customer}
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    raw_response = chain.run({
        "strategy": strategy,
        "customer": json.dumps(customer)
    })

    try:
        parsed = json.loads(raw_response)

        # Basic validation
        if "channel" not in parsed or "send_time" not in parsed:
            raise ValueError("Missing keys in LLM response")

        return parsed

    except Exception:
        # Defensive fallback based on simple rules
        open_rate = customer.get("open_rate", 0)
        click_rate = customer.get("click_rate", 0)

        if open_rate > 0.7 and click_rate > 0.3:
            return {"channel": "Email", "send_time": "Weekday morning"}
        elif open_rate > 0.4:
            return {"channel": "SMS", "send_time": "Afternoon"}
        else:
            return {"channel": "Call", "send_time": "Evening"}
