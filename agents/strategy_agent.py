import json
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def strategy_agent(llm, insight: str) -> dict:
    """
    Decide marketing strategy based on customer insight.
    Returns structured dict: {"strategy": "<value>"}
    """

    prompt = PromptTemplate(
        input_variables=["insight"],
        template="""
You are a marketing decision engine.

Choose EXACTLY ONE strategy from:
- Retention
- Discount
- Upsell
- DoNothing

IMPORTANT RULES:
- Return ONLY valid JSON
- Do NOT add explanation
- Do NOT add markdown
- Do NOT add extra text

Return JSON in this EXACT format:
{{
  "strategy": "<one value>"
}}

Customer Insight:
{insight}
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    raw_response = chain.run({"insight": insight})

    try:
        return json.loads(raw_response)
    except json.JSONDecodeError:
        # Defensive fallback
        return {"strategy": "DoNothing"}
