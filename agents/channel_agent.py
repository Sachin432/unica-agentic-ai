import json
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def channel_agent(llm, strategy: str) -> dict:
    """
    Decide communication channel and send time based on strategy.
    Returns structured output safe for orchestration.
    """

    prompt = PromptTemplate(
        input_variables=["strategy"],
        template="""
You are a marketing channel decision engine.

Given the campaign strategy below, choose EXACTLY ONE channel
and ONE send time.

ALLOWED CHANNELS:
- Email
- SMS
- Push

IMPORTANT RULES:
- Return ONLY valid JSON
- Do NOT add explanation
- Do NOT add markdown
- Do NOT add extra text

Return JSON in this EXACT format:
{{
  "channel": "<Email | SMS | Push>",
  "send_time": "<short description>"
}}

Campaign Strategy:
{strategy}
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    raw_response = chain.run({"strategy": strategy})

    try:
        return json.loads(raw_response)
    except json.JSONDecodeError:
        # Defensive fallback
        return {
            "channel": "Email",
            "send_time": "Weekday morning"
        }
